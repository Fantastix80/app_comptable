from pymongo import MongoClient
from datetime import datetime, timedelta


# ============================================ FONCTIONS CONCERNANT LA BDD ==================================================

def connect_db(username, password, ip, port):
    """
    Cette fonction permet de se connecter à la bdd.
    Elle prend en paramètre l'adresse ip et le port ou est stockée la bdd ainsi que le nom de la bdd.
    Elle renvoie l'object contenant la bdd.
    """

    global db
    db = None

    if port == "":
        connection_string = f"mongodb+srv://{username}:{password}@{ip}"
    else:
        connection_string = f"mongodb+srv://{username}:{password}@{ip}:{port}"

    try:
        client = MongoClient(connection_string)
        db = client.get_database("app_comptable")

        with open("config_db", "w") as config:
            config.write(username + "\n" + password + "\n" + ip + "\n" + port + "\n")
    except:
        print("Erreur lors de la connexion à la base de donnée...")

    return db

def insert_db(collectionName, typeOfInsertion, operation):
    """
    Cette fonction permet d'insérer des données dans la bdd.
    Elle prend en paramètre l'object qui contient la bdd, le nom de la collection dans laquelle insérer les données, le type d'insertion (one ou many) ainsi qu'un dictionnaire contenant les données à intégrer.
    Elle renvoie le ou les ids des dernières données insérées dans la bdd.
    """
    
    collection = db.get_collection(collectionName)

    if typeOfInsertion == "one":
        response = collection.insert_one(operation)
        last_inserted_id = response.inserted_id
    elif typeOfInsertion == "many":
        response = collection.insert_many(operation)
        last_inserted_id = response.inserted_ids

    return last_inserted_id

def update_db(collectionName, typeOfModification, data, new_type):

    collection = db.get_collection(collectionName)

    if typeOfModification == "one":
        date_temp = data[0].split(" ")
        date_formate_debut_str = date_temp[0].split("/")[2] + "-" + date_temp[0].split("/")[1] + "-" + date_temp[0].split("/")[0] + " " + date_temp[1] + ".000"
        date_formate_fin_str = date_temp[0].split("/")[2] + "-" + date_temp[0].split("/")[1] + "-" + date_temp[0].split("/")[0] + " " + date_temp[1] + ".999"
        date_formate_debut = datetime.strptime(date_formate_debut_str, "%Y-%m-%d %H:%M:%S.%f")
        date_formate_fin = datetime.strptime(date_formate_fin_str, "%Y-%m-%d %H:%M:%S.%f")

        filter = {"$and": [{"horodatage": {"$gte": date_formate_debut, "$lte": date_formate_fin}}, {"montant": float(data[2])}, {"motif": data[3]}]}
        new_values = {"$set": {"type": new_type}}
        collection.update_one(filter, new_values)

def getAllOperations(date, etat, montant, libelle):
    """
    Cette fonction permet de récupérer toutes les opérations stockées en bdd et les renvoie sous forme de tableau
    """

    collection = db.get_collection("operations")

    filter = []

    current_date_str = str(getDateTime()).split(" ")[0]
    current_date_str_formated = current_date_str.split("-")[2] + "/" + current_date_str.split("-")[1] + "/" + current_date_str.split("-")[0]

    if date != current_date_str_formated and date != "":
        date_debut_str = date.split("/")[2] + "-" + date.split("/")[1] + "-" + date.split("/")[0] + " 00:00:00"
        date_fin_str = date.split("/")[2] + "-" + date.split("/")[1] + "-" + date.split("/")[0] + " 23:59:59"

        date_debut = datetime.strptime(date_debut_str, "%Y-%m-%d %H:%M:%S")
        date_fin = datetime.strptime(date_fin_str, "%Y-%m-%d %H:%M:%S")

        filter.append({"horodatage": {"$gte": date_debut, "$lte": date_fin}})

    if etat != "":
        filter.append({"etat": etat})

    if montant != 0.00:
        filter.append({"$or": [{"debit": montant}, {"credit": montant}]})

    if libelle != "":
        filter.append({"libelle": {"$regex": libelle, "$options" : "i"}})

    if len(filter) > 1:
        data = collection.find({"$and": filter})
    elif len(filter) == 1:
        data = collection.find(filter[0])
    else:
        data = collection.find().sort("horodatage", -1)

    return data

def getSolde():
    collection = db.get_collection("operations")
    data = collection.find({"etat": "ACCEPTEE"})

    solde = 0.00
    for each_line in data:
        solde -= each_line["debit"]
        solde += each_line["credit"]

    return solde

def getSoldePrevisionnel():
    collection = db.get_collection("operations")
    filter = {"etat": {"$ne": "REFUSEE"}}
    data = collection.find(filter)

    solde = 0.00
    for each_line in data:
        solde -= each_line["debit"]
        solde += each_line["credit"]

    return solde

def getDateTime():
    """
    Cette fonction permet de renvoyer une date heure
    """

    return datetime.now()

def getDateTimeMinus24Hours():
    """
    Cette fonction permet de renvoyer une date heure
    """

    current_datetime = str(datetime.now()).split(".")[0]
    new_time_obj = datetime.strptime(current_datetime, "%Y-%m-%d %H:%M:%S") - timedelta(days=1)

    return new_time_obj

def formateDate(date):
    """
    Cette fonction permet de formater une date au format dateheure français.
    """

    date_temp = str(date).split(".")[0].split(" ")
    date_formate = date_temp[0].split("-")[2] + "/" + date_temp[0].split("-")[1] + "/" + date_temp[0].split("-")[0] + " " + date_temp[1]

    return date_formate

# ==================================== FIN DES FONCTIONS CONCERNANT LA BDD =========================================