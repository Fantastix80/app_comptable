import os
import sys

from interface import *
from fonctionsBDD import *

from Custom_Widgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # On vient charger le fichier .json
        loadJsonStyle(self, self.ui)

        # On vient connecter les boutons de navigation à une action
        self.ui.homeBtn.clicked.connect(lambda: self.switchPage("accueil", self.ui.homeBtn))
        self.ui.nouvelleOperationBtn.clicked.connect(lambda: self.switchPage("nouvelleOperation", self.ui.nouvelleOperationBtn))
        self.ui.historiqueOperationBtn.clicked.connect(lambda: self.switchPage("historiqueOperations", self.ui.historiqueOperationBtn))
        self.ui.parametreBtn.clicked.connect(lambda: self.switchPage("parametres", self.ui.parametreBtn))

        # On vient connecter les 2 boutons de la page nouvelle opération
        self.ui.annulerOperationBtn.clicked.connect(lambda: self.switchPage("accueil", self.ui.homeBtn))
        self.ui.validerOperationBtn.clicked.connect(lambda: self.inserer_nouvelle_operation(
            self.ui.typeOperationInput.currentText(),
            self.ui.etatOperationInput.currentText(),
            self.ui.montantOperationInput.value(),
            self.ui.libelleOperationInput.toPlainText(),
            ))
        
        # On vient définir la taille des colonnes du tableau de la page historique opérations
        self.ui.tableauHistoriqueOperations.setColumnWidth(0, 150)
        self.ui.tableauHistoriqueOperations.setColumnWidth(1, 150)
        self.ui.tableauHistoriqueOperations.setColumnWidth(2, 150)
        self.ui.tableauHistoriqueOperations.setColumnWidth(3, 150)
        self.ui.tableauHistoriqueOperations.setColumnWidth(4, 150)

        # On vient connecter les 2 boutons de la page historique opérations
        self.ui.supprimerFiltresBtn.clicked.connect(lambda: self.switchPage("historiqueOperations", self.ui.historiqueOperationBtn))
        self.ui.validerFiltresBtn.clicked.connect(lambda: self.populateTable(
            self.ui.filtreDateInput.date().toString("dd/MM/yyyy"),
            self.ui.filtreEtatInput.currentText(),
            self.ui.filtreMontantInput.value(),
            self.ui.filtreLibelleInput.text(),
            ))

        # On vient afficher les informations concernant les différentes pages
        self.ui.soldeMontant.setText(f"{self.format_montant(getSolde())} €")
        self.ui.soldePrevisionnelMontant.setText(f"{self.format_montant(getSoldePrevisionnel())} €")
        

        # On vient afficher la page
        self.show()

    def switchPage(self, page, buttonClicked):
        """
        Cette fonction permet de changer de page lors d'un clique sur un bouton de navigation.
        Elle prend en paramètre self, la page de destination (string) ainsi que le bouton cliqué (QPushButton).
        Elle ne renvoie rien.
        """
        for index in range(self.ui.mainPages.count()): # On vient parcourir toutes les pages présentes dans l'application
            if page == self.ui.mainPages.widget(index).objectName(): # Si le nom de la page est égale au nom souhaité.

                # On vient enlever le background des boutons de navigation
                self.ui.homeBtn.setStyleSheet(u"background-color: transparent;")
                self.ui.nouvelleOperationBtn.setStyleSheet(u"background-color: transparent;")
                self.ui.historiqueOperationBtn.setStyleSheet(u"background-color: transparent;")
                self.ui.parametreBtn.setStyleSheet(u"background-color: transparent;")

                # On vient rafraichir toutes les données dynamiques de l'application
                self.refresh_all_data()

                # On vient afficher la page désirée
                self.ui.mainPages.setCurrentIndex(index)

                # On vient mettre le background sur le bouton cliqué
                buttonClicked.setStyleSheet(u"background-color: #1f232a;")

    def inserer_nouvelle_operation(self, typeOperation, etatOperation, montantOperation, libelleOperation):
        """
        Cette fonction permet d'insérer une nouvelle opération en base de donnée en vérifiant au préalable l'intégrité des données en entrée.
        Elle prend en paramètre: le type d'opération, l'état de l'opération, le montant et el libelle.
        Elle ne renvoie rien.
        """

        if montantOperation != 0.00:
            if typeOperation == "DEBIT":
                operation = {"horodatage": getDateTime(),
                        "type": typeOperation,
                        "etat": etatOperation,
                        "debit": montantOperation,
                        "credit": 0.00,
                        "libelle": libelleOperation
                        }
            else:
                operation = {"horodatage": getDateTime(),
                        "type": typeOperation,
                        "etat": etatOperation,
                        "debit": 0.00,
                        "credit": montantOperation,
                        "libelle": libelleOperation
                        }
            insert_db("operations", "one", operation)
            self.switchPage("accueil", self.ui.homeBtn)
        else:
            print("Veuillez indiquer un montant valide")

    def refresh_all_data(self):
        # On vient afficher les informations concernant les différentes pages
        self.ui.soldeMontant.setText(f"{self.format_montant(getSolde())} €")
        self.ui.soldePrevisionnelMontant.setText(f"{self.format_montant(getSoldePrevisionnel())} €")

        # On vient raffraichir les éléments de la page nouvelle opération
        self.ui.typeOperationInput.setCurrentIndex(0) # On vient afficher la première valeur de la liste à choix
        self.ui.etatOperationInput.setCurrentIndex(0) # On vient afficher la première valeur de la liste à choix
        self.ui.montantOperationInput.setValue(0.00)
        self.ui.libelleOperationInput.clear()

        # On vient raffraichir les filtres de la page historique opérations
        dateStr = str(getDateTime()).split(" ")[0]
        qdate = QtCore.QDate.fromString(dateStr, "yyyy-MM-dd")
        self.ui.filtreDateInput.setDate(qdate)
        self.ui.filtreEtatInput.setCurrentIndex(0) # On vient afficher la première valeur de la liste à choix
        self.ui.filtreLibelleInput.clear()
        self.ui.filtreMontantInput.setValue(0.00)

        # On vient aussi raffraichir les données présentes dans le tableau historiques des opérations
        self.populateTable("", "", 0.00, "")
        
    def populateTable(self, date, etat, montant, libelle):
        """
        Cette fonction permet de remplir la tableau avec les données de la base de donnée.
        Elle prend en paramètre les filtres date, etat, montant et libelle afin de pouvoir récupérer les données filtrées si les filtres ont été remplies.
        Elle ne renvoie rien.
        """

        # On récupère toutes les données
        operations = getAllOperations(date, etat, montant, libelle)

        # On définit le nombre de ligne que contiendra le tableau
        self.ui.tableauHistoriqueOperations.setRowCount(len(list(operations.clone())))

        # On vient insérer chacune de ses lignes
        for index, operation in enumerate(operations):
            self.ui.tableauHistoriqueOperations.setItem(index, 0, QtWidgets.QTableWidgetItem(str(operation["horodatage"]).split(".")[0]))
            self.ui.tableauHistoriqueOperations.setItem(index, 1, QtWidgets.QTableWidgetItem(str(operation["type"])))
            self.ui.tableauHistoriqueOperations.setItem(index, 2, QtWidgets.QTableWidgetItem(str(operation["etat"])))
            self.ui.tableauHistoriqueOperations.setItem(index, 3, QtWidgets.QTableWidgetItem(self.format_montant(operation["debit"])))
            self.ui.tableauHistoriqueOperations.setItem(index, 4, QtWidgets.QTableWidgetItem(self.format_montant(operation["credit"])))
            self.ui.tableauHistoriqueOperations.setItem(index, 5, QtWidgets.QTableWidgetItem(str(operation["libelle"])))


    def format_montant(self, montant):
        try:
            montant_split = str(float(montant)).split(".")
            if len(montant_split[1]) != 2:
                montant_split[1] = (montant_split[1] + "00")[:2]
                result = montant_split[0] + "." + montant_split[1]
            else:
                result = str(montant)
        except:
            "Erreur lors du formatage du montant"
            result = None

        return result




username = "jean"
password = "1q4JPZeym7KkwsO5"
db_ip = "app-comptable.akieago.mongodb.net"
db_port = ""

# Connection à la bdd

connect_db(username, password, db_ip, db_port)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


"""
TO DO LIST:

- Designer un système de d'enregistrement de profil pour enregistrer différentes bdd et pouvoir rapidement switch entre chacunes.
- Intégrer le système permettant de choisir le profil désiré puis que la connection à la bonne bdd se fasse dans la foulée
- Faire en sorte que la personne arrive dans un premier temps sur la page de paramètre. Si elle tente d'aller dans les autres onglets sans choisir un profil: annuler l'action + mettre un message d'alerte.
- Mettre un message d'alerte lors d'un échec d'un enregistrement d'une nouvelle opération du au montant qui n'a pas été défini (à la place du print actuel)
- Ajouter dans la page nouvelle opération une façon de pouvoir associer l'opération à une date précise et non forcément la date heure actuel
- Styliser le tableau contenant les data
- Ajouter l'option permettant de pouvoir modifier l'état d'une opération
- Désactiver le possibilité de modifier les données depuis le tableau (même si cela n'impacte pas la bdd)
- Ajouter des graphiques pour remplir la page d'accueil

"""