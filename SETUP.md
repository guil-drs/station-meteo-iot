# Station Météo - Guide de setup pour l'équipe

Ce guide explique comment configurer le projet Django sur votre PC pour pouvoir travailler dessus et tester la page web avec les mesures simulées.

---

## 1️⃣ Prérequis

Avant de commencer, il faut s'assurer que votre ordinateur a tout ce qu’il faut pour faire tourner Django et le projet. Voici les étapes détaillées :

### a) Installer Python 3.10 ou plus récent

1. Allez sur le site officiel : https://www.python.org/downloads/
2. Téléchargez et installez la version recommandée pour votre système (Windows, macOS ou Linux).
3. Important sur Windows : cochez la case "Add Python to PATH" pendant l’installation.
4. Pour vérifier que Python est bien installé, ouvrez un terminal et tapez :
python --version
Vous devriez voir un numéro de version comme Python 3.14.0.

---

### b) Installer Git

1. Téléchargez Git : https://git-scm.com/downloads
2. Installez-le avec les options par défaut.
3. Vérifiez l’installation :
git --version
Vous devriez voir un numéro de version, par exemple git version 2.41.0.

---

### c) Installer VS Code (ou un autre éditeur)

- Téléchargez VS Code : https://code.visualstudio.com/
- Installez-le normalement.
- Facultatif mais conseillé : installez l’extension Python pour VS Code.

---

### d) Installer Mosquitto (optionnel pour MQTT)

Si vous voulez tester la partie IoT / MQTT :

1. Téléchargez Mosquitto pour votre système : https://mosquitto.org/download/
2. Installez-le et assurez-vous que la commande mosquitto fonctionne dans le terminal :
mosquitto -h
Vous devriez voir l’aide de Mosquitto s’afficher.

---

### e) Créer le fichier .gitignore pour le projet

Pour éviter de pousser le dossier venv ou la base de données SQLite sur GitHub, assurez-vous d’avoir un fichier .gitignore à la racine du projet avec au moins ces lignes :

venv/
db.sqlite3
__pycache__/
*.pyc

Cela empêche Git de suivre ces fichiers et dossiers inutiles.

---

### f) Le rôle du venv et comment l’utiliser

- À chaque fois que vous ouvrez le projet pour travailler, vous devez activer le venv pour que Python utilise les bonnes bibliothèques.  
- Sur Windows :
venv\Scripts\activate
- Sur macOS / Linux :
source venv/bin/activate
- Quand le venv est activé, le nom (venv) apparaît dans le terminal.  
- Une fois activé, vous pouvez lancer le serveur Django et installer des dépendances.
- Pour quitter le venv, tapez :
deactivate

Conseil : toujours activer le venv avant de faire python manage.py runserver ou d’installer de nouvelles bibliothèques.

---

## 2️⃣ Cloner le projet depuis GitHub

Ouvrez un terminal et tapez :

git clone https://github.com/guil-drs/station-meteo-iot.git
cd station-meteo-iot

---

## 3️⃣ Créer un environnement virtuel (recommandé)

python -m venv venv

Activez-le :

- Windows :
venv\Scripts\activate
- macOS / Linux :
source venv/bin/activate

---

## 4️⃣ Installer les dépendances

pip install -r requirements.txt

> Le fichier requirements.txt contient toutes les dépendances nécessaires :
Django==6.0.1
paho-mqtt==1.6.1

---

## 5️⃣ Lancer le serveur Django

Dans le terminal :

python manage.py runserver

Puis ouvrez votre navigateur sur :  
http://127.0.0.1:8000/meteo/demo/

Vous devriez voir la page avec les mesures simulées.

---

## 6️⃣ Modifier le code

Éditez les fichiers dans VS Code, par exemple :

- meteo/views.py pour la logique des mesures simulées
- meteo/templates/meteo/demo.html pour le frontend
- meteo/static/meteo/styles.css pour le style

Sauvegardez et rechargez la page dans le navigateur pour voir les changements.

---

## 7️⃣ Mettre à jour GitHub

Après avoir modifié des fichiers :

git add .
git commit -m "Description courte des modifications"
git push

Vos coéquipiers peuvent récupérer vos changements avec :

git pull

---

## 8️⃣ Notes importantes

- Ne pas inclure le dossier venv dans GitHub (il est déjà dans .gitignore)
- Ne pas modifier db.sqlite3 si vous voulez rester synchronisés
- Mosquitto est seulement nécessaire si vous voulez tester la partie IoT / MQTT
- Pour toute nouvelle dépendance Python, ajoutez-la dans requirements.txt avec :
pip freeze > requirements.txt

---

## 9️⃣ Bonus : Astuces

- VS Code propose un panneau Source Control pour faire git add / commit / push sans passer par le terminal.
- Utilisez des messages clairs pour les commits, par exemple : "Ajout graphique de l'humidité" ou "Correction du style CSS".
