# Projet Python : Maison Connectée Intelligente (Smart Home Simulation)

Ce projet est une **simulation complète d'une maison connectée** en Python.  
Il utilise la **programmation orientée objet** pour modéliser des pièces, des capteurs, des appareils, et intègre une **logique automatisée** qui réagit aux conditions environnementales simulées.

---

## Fonctionnalités principales

- Structure POO avec les classes : `MaisonConnecter`, `Piece`, `Capteur`, `Appareil`
- Capteurs de température
- Appareils (chauffage, lampe, TV, etc.) activés/désactivés automatiquement selon la température d'une piece
- Sauvegarde des mesures dans un fichier CSV (`analyser.csv`)
- Génération automatique d’un graphe PDF (`bilan_temp_maison.pdf`)
- Envoi du graphe sur le bot https://t.me/iot_devperso_bot

---

##  Technologies utilisées

- `Python` 
- `matplotlib` pour les graphiques
- `requests` pour l’API Telegram
- `csv` pour l’enregistrement des données
- `random` pour simuler les valeurs des capteurs

## Installation & lancement

1. Clone ce dépôt :
```shell
git clone https://github.com/ton-user/maison-connectee.git
```
```shell
cd maison-connectee
```
Faites la commande : 
```shell
pip install matplotlib requests
```
Pensez à remplacer dans le fichier python 
```shell
TOKEN = "USER_CHAT_ID" Avec votre ID à vous
```

puis 

``` SHELL
python simulateur.py 
```
