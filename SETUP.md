# Station Météo - Guide de setup pour l'équipe

Ce guide explique comment configurer le projet Django sur votre PC pour pouvoir travailler dessus et tester la page web avec les mesures simulées.

---

## 1️⃣ Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python 3.10+
- Git
- VS Code ou un autre éditeur de code
- Mosquitto (optionnel pour tester la partie MQTT)

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

pip install django paho-mqtt

Si un fichier requirements.txt est présent, vous pouvez aussi faire :

pip install -r requirements.txt

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

- Ne pas inclure le dossier venv dans GitHub
- Ne pas modifier db.sqlite3 si vous voulez rester synchronisés
- Mosquitto est seulement nécessaire si vous voulez tester la partie IoT / MQTT
- Pour toute nouvelle dépendance Python, ajoutez-la dans requirements.txt avec :

pip freeze > requirements.txt

---

## 9️⃣ Bonus : Astuces

- VS Code propose un panneau Source Control pour faire git add / commit / push sans passer par le terminal.
- Utilisez des messages clairs pour les commits, par exemple : "Ajout graphique de l'humidité" ou "Correction du style CSS".
