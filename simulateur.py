import random
from datetime import datetime
import time
import csv
import requests
import matplotlib.pyplot as plt

TOKEN = "YOUR_TOKKEN"  # Replace with your actual chat ID

# You can add the bot telegram it's iot_developper_bot
TOKEN_BOT = "7771488436:AAGK1ePK7i9R3CZDFLrugLdkk6VYIXe-970"

def envoyer_pdf_telegram(token_bot, chat_id, chemin_fichier):
    url = f"https://api.telegram.org/bot{token_bot}/sendDocument"
    with open(chemin_fichier, "rb") as fichier:
        data = {"chat_id": chat_id}
        files = {"document": fichier}
        response = requests.post(url, data=data, files=files)
    return response

def genere_graphe(maison):
    temperature_data = []

    for piece in maison.pieces:
        for capteur in piece.list_capteur:
            if capteur.type == "température":
                valeur = capteur.mesurer()
                temperature_data.append((piece.name, valeur))

    labels = [t[0] for t in temperature_data]
    valeurs = [t[1] for t in temperature_data]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, valeurs, color='skyblue')
    plt.title("🌡️ Température actuelle par pièce")
    plt.ylabel("Température (°C)")
    plt.ylim(0, 40)
    plt.tight_layout()
    plt.savefig("bilan_temp_maison.pdf")
    plt.close()





def analyser_to_csv(maison): 
    with open("analyser.csv", "a", newline="") as file:
        writer = csv.writer(file)
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for piece in maison.pieces:
            for capteur in piece.list_capteur:
                valeur = capteur.mesurer()
                writer.writerow([horodatage, piece.name, capteur.name, valeur, capteur.unite])


class Capteur:
    def __init__(self, name, type, unite):
        self.name = name
        self.type = type
        self.unite = unite

    def mesurer(self):
        if self.type == "température":
            return round(random.uniform(10.0, 30.0), 1)
        elif self.type == "luminosité":
            return random.randint(-10, 30)
        return None


class Appareil:
    def __init__(self, name):
        self.name = name
        self.etat = False
    def activer(self):
        self.etat = True
    def desactiver(self):
        self.etat = False
    def afficher_etat(self):
        etat_txt = "allumé" if self.etat else "éteint"
        print(f"🔌 {self.name} : {etat_txt}")


class Piece:
    def __init__(self, name):
        self.name = name
        self.list_capteur = []
        self.list_appareil = []
    def analyser_et_reagir(self):
        for capteur in self.list_capteur:
            valeur = capteur.mesurer()
            print(f"Mesure du capteur {capteur.name} : {valeur}{capteur.unite}")

            for appareil in self.list_appareil:
                if capteur.type == "température":
                    if valeur < 18:
                        print(f"Il fait froid ({valeur}°C) → {appareil.name} activé")
                        appareil.activer()
                    elif valeur > 25:
                        print(f"Il fait chaud ({valeur}°C) → {appareil.name} désactivé")
                        appareil.desactiver()
        

class MaisonConnecter:
    def __init__(self):
        self.pieces = []

    def ajouter_piece(self, piece):
        self.pieces.append(piece)

    def simuler_maison(self):
        print(f"---------------------- Analyse ----------------------\n")
        for piece in self.pieces:
            print(f"Pièce : {piece.name}")
            print(f"Etat chauffage {piece.analyser_et_reagir()}")
            for appareil in piece.list_appareil:
                print(f"Etat Appareil {appareil.afficher_etat()}")
        time.sleep(2)
        analyser_to_csv(self)
        genere_graphe(self)
        print(f"---------------------- Fin Analyse ----------------------\n")

if __name__ == "__main__":
    maison = MaisonConnecter()


    salon = Piece("Salon")
    salon.list_capteur.append(Capteur("ThermoSalon", "température", "°C"))
    salon.list_appareil.append(Appareil("Télé"))
    salon.list_appareil.append(Appareil("Lampe"))
    maison.ajouter_piece(salon)

    cuisine = Piece("Cuisine")
    cuisine.list_capteur.append(Capteur("ThermoCuisine", "température", "°C"))
    cuisine.list_appareil.append(Appareil("Hotte"))
    cuisine.list_appareil.append(Appareil("Lumière plafond"))
    maison.ajouter_piece(cuisine)

    chambre1 = Piece("Chambre de Tom")
    chambre1.list_capteur.append(Capteur("ThermoChambreTom", "température", "°C"))
    chambre1.list_appareil.append(Appareil("Chauffage électrique"))
    chambre1.list_appareil.append(Appareil("Lampe de chevet"))
    maison.ajouter_piece(chambre1)

    chambre2 = Piece("Chambre d’amis")
    chambre2.list_capteur.append(Capteur("ThermoChambreAmis", "température", "°C"))
    chambre2.list_appareil.append(Appareil("Radiateur"))
    maison.ajouter_piece(chambre2)

    salle_bain = Piece("Salle de bain")
    salle_bain.list_capteur.append(Capteur("ThermoSalleDeBain", "température", "°C"))
    salle_bain.list_appareil.append(Appareil("Sèche-serviette"))
    maison.ajouter_piece(salle_bain)

    maison.simuler_maison()
    envoyer_pdf_telegram(TOKEN_BOT, TOKEN, "bilan_temp_maison.pdf")

