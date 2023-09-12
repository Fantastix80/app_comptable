import customtkinter
from tkinter import ttk
from tkcalendar import *
from pymongo import MongoClient
from datetime import datetime, timedelta

# Activation du mode sombre de la fenêtre
customtkinter.set_appearance_mode("dark")

# Variables globales
APP_NAME = "Application comptable"
SOLDE = 0.00
SOLDE_PREVISIONNEL = 0.00

# Variables de connexion à la bdd
# username = "jean"
# password = "1q4JPZeym7KkwsO5"
# db_ip = "app-comptable.akieago.mongodb.net"
# db_port = ""

# ==================================== FONCTIONS CONCERNANT L'APPLICATION =================================================

def showConfig(errors = {}, info_connexion = []):
    global config
    config = customtkinter.CTk() # On crée l'application
    config.title(APP_NAME) # On définie un titre

    # TITRE
    titre = customtkinter.CTkLabel(config, text="Connexion à la base de donnée", font=customtkinter.CTkFont(family="Helvetica", size=40, weight="bold"))
    titre.grid(row=0, column=0, columnspan=2, pady=(50,50), padx=(50,50))

    if len(info_connexion) < 1:
        # SHOW ERRORS
        if "erreur" in errors:
            erreur = customtkinter.CTkLabel(config, text=errors["erreur"], font=customtkinter.CTkFont(family="Helvetica", size=18), text_color="red")
            erreur.grid(row=1, column=0, columnspan=2, pady=(0,30))

        # LABELS
        identifiant_titre = customtkinter.CTkLabel(config, text="Identifiant:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
        identifiant_titre.grid(row=2, column=0, pady=(0,20), padx=(50, 20), sticky="w")

        mdp_titre = customtkinter.CTkLabel(config, text="Mot de passe:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
        mdp_titre.grid(row=3, column=0, pady=(0,20), padx=(50, 20), sticky="w")

        ip_titre = customtkinter.CTkLabel(config, text="IP:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
        ip_titre.grid(row=4, column=0, pady=(0,20), padx=(50, 20), sticky="w")

        port_titre = customtkinter.CTkLabel(config, text="Port:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
        port_titre.grid(row=5, column=0, pady=(0,30), padx=(50, 20), sticky="w")

        # INPUTS
        identifiant_input = customtkinter.CTkEntry(config, width=350)
        identifiant_input.grid(row=2, column=1, pady=(0,20), sticky="w")

        mdp_input = customtkinter.CTkEntry(config, width=350)
        mdp_input.grid(row=3, column=1, pady=(0,20), sticky="w")

        ip_input = customtkinter.CTkEntry(config, width=350)
        ip_input.grid(row=4, column=1, pady=(0,20), sticky="w")

        port_input = customtkinter.CTkEntry(config, width=350)
        port_input.grid(row=5, column=1, pady=(0,30), sticky="w")

        # BOUTON
        connexion = customtkinter.CTkButton(config, text="Connexion", font=customtkinter.CTkFont(family="Helvetica", size=18, weight="bold"), fg_color="green", command=lambda:connect_db(config, identifiant_input.get(), mdp_input.get(), ip_input.get(), port_input.get()))
        connexion.grid(row=6, column=0, columnspan=2, pady=(0,50), ipady=10, ipadx=20)

        config.grid_columnconfigure(1, weight=1)

    else:

        # TITRE
        sous_titre = customtkinter.CTkLabel(config, text="Voulez-vous utiliser les paramètres de connexion sauvergardée ?", font=customtkinter.CTkFont(family="Helvetica", size=20, weight="bold"), text_color="red")
        sous_titre.grid(row=1, column=0, columnspan=2, pady=(0,50), padx=(20,20))

        # LABELS
        identifiant_titre = customtkinter.CTkLabel(config, text="Identifiant:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
        identifiant_titre.grid(row=2, column=0, pady=(0,20), padx=(50, 20), sticky="w")

        mdp_titre = customtkinter.CTkLabel(config, text="Mot de passe:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
        mdp_titre.grid(row=3, column=0, pady=(0,20), padx=(50, 20), sticky="w")

        ip_titre = customtkinter.CTkLabel(config, text="IP:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
        ip_titre.grid(row=4, column=0, pady=(0,20), padx=(50, 20), sticky="w")

        port_titre = customtkinter.CTkLabel(config, text="Port:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
        port_titre.grid(row=5, column=0, pady=(0,30), padx=(50, 20), sticky="w")

        # INPUTS
        identifiant_input = customtkinter.CTkEntry(config, width=350)
        identifiant_input.insert(0, info_connexion[0])
        identifiant_input.configure(state="disabled")
        identifiant_input.grid(row=2, column=1, pady=(0,20), sticky="w")

        mdp_input = customtkinter.CTkEntry(config, width=350)
        mdp_input.insert(0, info_connexion[1])
        mdp_input.configure(state="disabled")
        mdp_input.grid(row=3, column=1, pady=(0,20), sticky="w")

        ip_input = customtkinter.CTkEntry(config, width=350)
        ip_input.insert(0, info_connexion[2])
        ip_input.configure(state="disabled")
        ip_input.grid(row=4, column=1, pady=(0,20), sticky="w")

        port_input = customtkinter.CTkEntry(config, width=350)
        port_input.insert(0, info_connexion[3])
        port_input.configure(state="disabled")
        port_input.grid(row=5, column=1, pady=(0,30), sticky="w")

        # BOUTON
        non = customtkinter.CTkButton(config, text="Non", font=customtkinter.CTkFont(family="Helvetica", size=18, weight="bold"), fg_color="red", command=destroyConfig)
        non.grid(row=6, column=0, pady=(0,50), ipady=10, ipadx=20, sticky="e")

        oui = customtkinter.CTkButton(config, text="Oui", font=customtkinter.CTkFont(family="Helvetica", size=18, weight="bold"), fg_color="green", command=lambda:connect_db(config, info_connexion[0], info_connexion[1], info_connexion[2], info_connexion[3]))
        oui.grid(row=6, column=1, pady=(0,50), padx=(50, 0), ipady=10, ipadx=20, sticky="w")

    config.configure(fg_color="#1a1a1a") # On définie le forground (background)
    config.resizable(width=False, height=False) # On interdit le redimensionnement de la page
    config.mainloop() # On vient faire tourner la boucle de l'application

def destroyConfig():
    config.destroy()
    showConfig()

def startApp():
    global app
    app = customtkinter.CTk() # On crée l'application
    app.title(APP_NAME) # On définie un titre

    raise_frame("mainPage") # On vient créer et afficher la page principale

    app.configure(fg_color="#1a1a1a") # On définie le forground (background)
    app.resizable(width=False, height=False) # On interdit le redimensionnement de la page
    app.mainloop() # On vient faire tourner la boucle de l'application

def raise_frame(page, currentFrame = None):
    """
    Cette fonction permet d'afficher la bonne frame à l'écran.
    Elle prend en paramètre un string contenant le nom de la page à afficher ainsi que la frame actuelle.
    Elle ne renvoie rien.
    """

    if currentFrame != None: # Si la frame actuelle n'est pas la valeur par défaut
        currentFrame.destroy() # On la supprime

        # Puis on vient générer la frame sur laquelle on cherche à se rendre
        if page == "mainPage":
            mainPage = customtkinter.CTkFrame(app) # On crée une frame
            mainPage.grid(row=0, column=0, sticky='news') # On initie la grille
            mainPage.configure(fg_color="#1a1a1a") # On définie le forground (background)
            build_mainPage(mainPage) # On vient construire la page
            mainPage.tkraise() # puis finalement on affiche la frame à l'écran
        elif page == "insertOperation":
            insertOperation = customtkinter.CTkFrame(app)
            insertOperation.grid(row=0, column=0, sticky='news')
            insertOperation.configure(fg_color="#1a1a1a")
            build_insertOperation(insertOperation)
            insertOperation.tkraise()
        elif page == "historiqueOperations":
            global historiqueOperations
            historiqueOperations = customtkinter.CTkFrame(app)
            historiqueOperations.grid(row=0, column=0, sticky='news')
            historiqueOperations.configure(fg_color="#1a1a1a")
            build_historiqueOperations(historiqueOperations)
            historiqueOperations.tkraise()
        
    else: # Si il n'y a pas de frame actuelle, cela signifie qu'on se situe au lancement de l'application alors on vient simplement construire la frame principale
        mainPage = customtkinter.CTkFrame(app)
        mainPage.grid(row=0, column=0, sticky='news')
        mainPage.configure(fg_color="#1a1a1a")
        build_mainPage(mainPage)
        mainPage.tkraise()

    

def build_mainPage(mainPage):
    """
    Cette fonction permet d'initialiser tous les éléments que contiendra la page et de les placer sur celle-ci.
    """

    # Actualisation des soldes
    SOLDE = getSolde()
    SOLDE_PREVISIONNEL = getSoldePrevisionnel()

    # Formatage des soldes
    solde_split = str(SOLDE).split(".")
    if len(solde_split[1]) == 1:
        SOLDE = solde_split[0] + "." + solde_split[1] + "0"
    elif len(solde_split[1]) == 2:
        SOLDE = solde_split[0] + ".00"

    solde_split = str(SOLDE_PREVISIONNEL).split(".")
    if len(solde_split[1]) == 1:
        SOLDE_PREVISIONNEL = solde_split[0] + "." + solde_split[1] + "0"
    elif len(solde_split[1]) == 2:
        SOLDE_PREVISIONNEL = solde_split[0] + ".00"

    # TITRE DE L'APPLICATION
    titre = customtkinter.CTkLabel(mainPage, text=APP_NAME, font=customtkinter.CTkFont(family="Helvetica", size=40, weight="bold"))
    titre.grid(row=0, column=0, columnspan=3, pady=(50,50))

    # SOLDE
    solde = customtkinter.CTkLabel(mainPage, text=f"Solde:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
    solde.grid(row=1, column=0, sticky="w", padx=(50, 0), pady=(0,50))

    solde_a_venir = customtkinter.CTkLabel(mainPage, text=f"Solde prévisionnel:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
    solde_a_venir.grid(row=2, column=0, sticky="w", padx=(50,0), pady=(0,50))

    if float(SOLDE) >= 0:
        montant_solde = customtkinter.CTkLabel(mainPage, text=f"{SOLDE} €", font=customtkinter.CTkFont(family="Helvetica", size=27), text_color="green")
    else:
        montant_solde = customtkinter.CTkLabel(mainPage, text=f"{SOLDE} €", font=customtkinter.CTkFont(family="Helvetica", size=27), text_color="red")
    montant_solde.grid(row=1, column=1, sticky="w", padx=(30,0), pady=(0,50))

    if float(SOLDE_PREVISIONNEL) >= 0:
        montant_solde_a_venir = customtkinter.CTkLabel(mainPage, text=f"{SOLDE_PREVISIONNEL} €", font=customtkinter.CTkFont(family="Helvetica", size=27), text_color="green")
    else:
        montant_solde_a_venir = customtkinter.CTkLabel(mainPage, text=f"{SOLDE_PREVISIONNEL} €", font=customtkinter.CTkFont(family="Helvetica", size=27), text_color="red")
    montant_solde_a_venir.grid(row=2, column=1, sticky="w", padx=(30,0), pady=(0,50))

    # BOUTONS
    btn_insert_operation = customtkinter.CTkButton(mainPage, text="Insérer une nouvelle opération", command=lambda:raise_frame("insertOperation", mainPage), font=customtkinter.CTkFont(family="Helvetica", size=18))
    btn_insert_operation.grid(row=1, column=2, padx=(50,50), pady=(0,50), ipady=10, ipadx=20)

    btn_historique_operation = customtkinter.CTkButton(mainPage, text="Historique des opérations", command=lambda:raise_frame("historiqueOperations", mainPage), font=customtkinter.CTkFont(family="Helvetica", size=18))
    btn_historique_operation.grid(row=2, column=2, padx=(50,50), pady=(0,50), ipady=10, ipadx=20)


def build_insertOperation(insertOperation):
    """
    Cette fonction permet d'initialiser tous les éléments que contiendra la page et de les placer sur celle-ci.
    """

    # CONFIGURATION DE LA GRILLE
    insertOperation.grid_rowconfigure(0, weight=1)
    insertOperation.grid_rowconfigure(1, weight=1)
    insertOperation.grid_rowconfigure(2, weight=1)
    insertOperation.grid_rowconfigure(3, weight=1)
    insertOperation.grid_rowconfigure(4, weight=1)
    insertOperation.grid_columnconfigure(0, weight=1)
    insertOperation.grid_columnconfigure(1, weight=1)

    # TITRE DE LA PAGE
    titre = customtkinter.CTkLabel(insertOperation, text="Insérer une nouvelle opération", font=customtkinter.CTkFont(family="Helvetica", size=40, weight="bold"))
    titre.grid(row=0, column=0, columnspan=2, pady=(50,50), padx=(50,50))

    # LABELS
    type_operation = customtkinter.CTkLabel(insertOperation, text="Type d'opération:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
    type_operation.grid(row=1, column=0, pady=(0,20), padx=(0,20), sticky="e")

    montant = customtkinter.CTkLabel(insertOperation, text="Montant:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
    montant.grid(row=2, column=0, pady=(0,20), padx=(0,20), sticky="e")

    motif = customtkinter.CTkLabel(insertOperation, text="Motif:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
    motif.grid(row=3, column=0, pady=(0,30), padx=(0,20), sticky="e")

    # INPUTS
    type_liste = customtkinter.CTkComboBox(insertOperation, state="readonly", values=["EN ATTENTE", "ACCEPTEE", "REFUSEE"])
    type_liste.set("EN ATTENTE")
    type_liste.grid(row=1, column=1, pady=(0,20), sticky="w")

    montant_input = customtkinter.CTkEntry(insertOperation, width=300)
    montant_input.grid(row=2, column=1, pady=(0,20), sticky="w")

    motif_input = customtkinter.CTkEntry(insertOperation, width=300)
    motif_input.grid(row=3, column=1, pady=(0,30), sticky="w")

    # BOUTONS
    btn_annuler = customtkinter.CTkButton(insertOperation, text="Annuler", command=lambda:raise_frame("mainPage", insertOperation), font=customtkinter.CTkFont(family="Helvetica", size=18), fg_color="red")
    btn_annuler.grid(row=4, column=0, pady=(0,50), padx=(50,0), ipady=10, ipadx=20, sticky="e")

    btn_valider = customtkinter.CTkButton(insertOperation, text="Valider", command=lambda:verify_input(insertOperation, type_liste.get(), montant_input.get(), motif_input.get()), font=customtkinter.CTkFont(family="Helvetica", size=18), fg_color="green")
    btn_valider.grid(row=4, column=1, pady=(0,50), padx=(50,0), ipady=10, ipadx=20, sticky="w")

def build_historiqueOperations(historiqueOperations):
    """
    Cette fonction permet d'initialiser tous les éléments que contiendra la page et de les placer sur celle-ci.
    """

    # BOUTON RETOUR
    retour = customtkinter.CTkButton(historiqueOperations, text="<- Retour", font=customtkinter.CTkFont(family="Helvetica", size=18, weight="bold"), command=lambda:raise_frame("mainPage", historiqueOperations))
    retour.grid(row=0, column=0, columnspan=5, sticky="w", padx=(20, 0), pady=(20, 0))

    # TITRE DE LA PAGE
    titre = customtkinter.CTkLabel(historiqueOperations, text="Historique des opérations", font=customtkinter.CTkFont(family="Helvetica", size=32, weight="bold"))
    titre.grid(row=1, column=0, columnspan=5, pady=(20,30))

    # FILTRES DE RECHERCHE
    titre_date = customtkinter.CTkLabel(historiqueOperations, text="Entrez une date:")
    titre_date.grid(row=2, column=1, pady=(0,10))

    titre_type = customtkinter.CTkLabel(historiqueOperations, text="Sélectionner un type:")
    titre_type.grid(row=2, column=2, pady=(0,10))

    titre_montant = customtkinter.CTkLabel(historiqueOperations, text="Entrez un montant:")
    titre_montant.grid(row=2, column=3, pady=(0,10))

    titre_motif = customtkinter.CTkLabel(historiqueOperations, text="Entrez votre recherche de motif:")
    titre_motif.grid(row=2, column=4, pady=(0,10))

    titre_filtre = customtkinter.CTkLabel(historiqueOperations, text="Filtres:")
    titre_filtre.grid(row=3, column=0, pady=(0,20))

    global filtre_date
    filtre_date = customtkinter.CTkEntry(historiqueOperations)
    filtre_date.grid(row=3, column=1, pady=(0,20))
    filtre_date.insert(0, "dd/mm/yyyy")
    filtre_date.bind("<1>", pick_date)

    type_input = customtkinter.CTkComboBox(historiqueOperations, state="readonly", values=["", "EN ATTENTE", "ACCEPTEE", "REFUSEE"])
    type_input.set("")
    type_input.grid(row=3, column=2, pady=(0,20))

    montant_input = customtkinter.CTkEntry(historiqueOperations)
    montant_input.grid(row=3, column=3, pady=(0,20))

    motif_input = customtkinter.CTkEntry(historiqueOperations)
    motif_input.grid(row=3, column=4, pady=(0,20))

    valide_filtre = customtkinter.CTkButton(historiqueOperations, text="Valider les filtres", font=customtkinter.CTkFont(family="Helvetica", size=18, weight="bold"), command=lambda:populateTable(historiqueOperations, filtre_date.get(), type_input.get(), montant_input.get(), motif_input.get()))
    valide_filtre.grid(row=4, column=2, columnspan=2, pady=(0,20))

    # TABLEAU
    populateTable(historiqueOperations)

    modifier_selection = customtkinter.CTkButton(historiqueOperations, text="Modifier l'opération selectionnée", font=customtkinter.CTkFont(family="Helvetica", size=18, weight="bold"), command=lambda:showModifyPage(table.item(table.selection()[0])["values"]))
    modifier_selection.grid(row=6, column=2, columnspan=2, pady=(20,20), sticky="nesw")

def populateTable(historiqueOperations, date = "dd/mm/yyyy", type = "", montant = "", motif = ""):
    global table
    table = ttk.Treeview(historiqueOperations, columns=("Horodatage", "Type", "Montant", "Motif"), show = "headings", selectmode="browse")
    table.heading("Horodatage", text = "Horodatage")
    table.heading("Type", text = "Type")
    table.heading("Montant", text = "Montant")
    table.heading("Motif", text = "Motif")
    table.grid(row=5, column=0, columnspan=5)

    operations = getAllOperations(date, type, montant, motif)

    for idx, operation in enumerate(operations):
        date_formate = formateDate(operation["horodatage"])
        table.insert(parent = "", index = idx, values = (date_formate, operation["type"], operation["montant"], operation["motif"]))

def showModifyPage(data):

    modify_window = customtkinter.CTkToplevel()
    modify_window.title("Modifier l'opération sélectionnée")

    # CONFIGURATION DE LA GRILLE
    modify_window.grid_rowconfigure(0, weight=1)
    modify_window.grid_rowconfigure(1, weight=1)
    modify_window.grid_rowconfigure(2, weight=1)
    modify_window.grid_rowconfigure(3, weight=1)
    modify_window.grid_rowconfigure(4, weight=1)
    modify_window.grid_columnconfigure(0, weight=1)
    modify_window.grid_columnconfigure(1, weight=1)

    # TITRE DE LA PAGE
    titre = customtkinter.CTkLabel(modify_window, text="Modifier l'opération sélectionnée", font=customtkinter.CTkFont(family="Helvetica", size=40, weight="bold"))
    titre.grid(row=0, column=0, columnspan=2, pady=(50,50), padx=(50,50))

    # LABELS
    type_operation = customtkinter.CTkLabel(modify_window, text="Type d'opération:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
    type_operation.grid(row=1, column=0, pady=(0,20), padx=(0,20), sticky="e")

    montant = customtkinter.CTkLabel(modify_window, text="Montant:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
    montant.grid(row=2, column=0, pady=(0,20), padx=(0,20), sticky="e")

    motif = customtkinter.CTkLabel(modify_window, text="Motif:", font=customtkinter.CTkFont(family="Helvetica", size=27, weight="bold"))
    motif.grid(row=3, column=0, pady=(0,30), padx=(0,20), sticky="e")

    # INPUTS
    type_liste = customtkinter.CTkComboBox(modify_window, state="readonly", values=["EN ATTENTE", "ACCEPTEE", "REFUSEE"])
    type_liste.set(data[1])
    type_liste.grid(row=1, column=1, pady=(0,20), sticky="w")

    montant_input = customtkinter.CTkEntry(modify_window, width=300)
    montant_input.insert(0, data[2])
    montant_input.configure(state="disabled")
    montant_input.grid(row=2, column=1, pady=(0,20), sticky="w")

    motif_input = customtkinter.CTkEntry(modify_window, width=300)
    motif_input.insert(0, data[3])
    motif_input.configure(state="disabled")
    motif_input.grid(row=3, column=1, pady=(0,30), sticky="w")

    # BOUTONS
    btn_annuler = customtkinter.CTkButton(modify_window, text="Annuler", command=lambda:modify_window.destroy(), font=customtkinter.CTkFont(family="Helvetica", size=18), fg_color="red")
    btn_annuler.grid(row=4, column=0, pady=(0,50), padx=(50,0), ipady=10, ipadx=20, sticky="e")

    btn_valider = customtkinter.CTkButton(modify_window, text="Modifier", command=lambda:modifyType(modify_window, data, type_liste.get()), font=customtkinter.CTkFont(family="Helvetica", size=18), fg_color="green")
    btn_valider.grid(row=4, column=1, pady=(0,50), padx=(50,0), ipady=10, ipadx=20, sticky="w")

def modifyType(modify_window, data, new_type):
    
    if data[1] != new_type:
        update_db("operations", "one", data, new_type)
        populateTable(historiqueOperations)

    modify_window.destroy()

    

def pick_date(event):
    global date_window
    global cal
    date_window = customtkinter.CTkToplevel()
    date_window.grab_set()
    date_window.title("Choisissez une date")
    cal = Calendar(date_window, selectmode="day", date_pattern="dd/mm/y")
    cal.pack()

    submit_btn = customtkinter.CTkButton(date_window, text="Valider", command=grab_date)
    submit_btn.pack()

def grab_date():
    filtre_date.delete(0, 10)
    filtre_date.insert(0, cal.get_date())
    date_window.destroy()


# ===================================== FIN DES FONCTIONS CONCERNANT L'APPLICATION ==========================================

# ============================================ FONCTIONS CONCERNANT LA BDD ==================================================

def connect_db(config, username, password, ip, port):
    """
    Cette fonction permet de se connecter à la bdd.
    Elle prend en paramètre l'adresse ip et le port ou est stockée la bdd ainsi que le nom de la bdd.
    Elle renvoie l'object contenant la bdd.
    """

    config.destroy()

    if port == "":
        connection_string = f"mongodb+srv://{username}:{password}@{ip}"
    else:
        connection_string = f"mongodb+srv://{username}:{password}@{ip}:{port}"

    try:
        client = MongoClient(connection_string)
        global db
        db = client.get_database("app_comptable")

        with open("config_db", "w") as config:
            config.write(username + "\n" + password + "\n" + ip + "\n" + port + "\n")

        startApp()
    except:
        showConfig({"erreur": "La connexion à la base de donnée a échoué..."})

def insert_db(db, collectionName, typeOfInsertion, operation):
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

def getAllOperations(date, type, montant, motif):
    """
    Cette fonction permet de récupérer toutes les opérations stockées en bdd et les renvoie sous forme de tableau
    """
    
    collection = db.get_collection("operations")

    filter = []

    if date != "dd/mm/yyyy":
        date_debut_str = date.split("/")[2] + "-" + date.split("/")[1] + "-" + date.split("/")[0] + " 00:00:00"
        date_fin_str = date.split("/")[2] + "-" + date.split("/")[1] + "-" + date.split("/")[0] + " 23:59:59"

        date_debut = datetime.strptime(date_debut_str, "%Y-%m-%d %H:%M:%S")
        date_fin = datetime.strptime(date_fin_str, "%Y-%m-%d %H:%M:%S")

        filter.append({"horodatage": {"$gte": date_debut, "$lte": date_fin}})

    if type != "":
        filter.append({"type": type})

    if montant != "":
        try:
            filter.append({"montant": float(montant)})
        except:
            filter.append({"montant": "erreur de recherche"})

    if motif != "":
        filter.append({"motif": {"$regex": motif, "$options" : "i"}})


    if len(filter) > 1:
        data = collection.find({"$and": filter})
    elif len(filter) == 1:
        data = collection.find(filter[0])
    else:
        data = collection.find().sort("horodatage", -1)

    return data

def getSolde():
    collection = db.get_collection("operations")
    data = collection.find({"type": "ACCEPTEE"})

    solde = 0.00
    for each_line in data:
        solde += float(each_line["montant"])

    return solde

def getSoldePrevisionnel():
    collection = db.get_collection("operations")
    filter = {"type": {"$ne": "REFUSEE"}}
    data = collection.find(filter)

    solde = 0.00
    for each_line in data:
        solde += float(each_line["montant"])

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

# ==================================== FONCTIONS DE VERIFICATIONS DES INPUTS =======================================

def verify_input(currentFrame, type, montant, motif):
    if verify_montant(montant) and verify_motif(motif):
        montant = str(montant).replace(",", ".")
        operation = {"horodatage": getDateTime(),
                     "type": type,
                     "montant": float(montant),
                     "motif": motif
                    }
        insert_db(db, "operations", "one", operation)
        raise_frame("mainPage", currentFrame)
    else:
        raise_frame("insertOperation", currentFrame)

def verify_montant(montant):

    montant = str(montant).replace(",", ".")

    try:
        if len(str(montant)) > 0 and float(montant):
            rep = True
        else:
            rep = False
    except:
        rep = False

    return rep

def verify_motif(motif):

    rep = False
    if len(str(motif)) > 0:
        rep = True

    return rep


# ==================================== FIN DES FONCTIONS DE VERIFICATIONS ==========================================

try:
    with open("config_db", "r") as config_info:
        info = []

        for line in config_info.readlines():
            info.append(line.rstrip("\n"))

        info_formate = [info[0], info[1], info[2], info[3]]
except:
    info_formate = []

showConfig({}, info_formate)
