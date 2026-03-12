import paho.mqtt.client as mqtt #librairie mqtt
import json # pour lire les fichiers json envoyés par l'esp32
from django.conf import settings
# from .models import DonneeMeteo # pour stocker les données par la suite


def on_connect(client, userdata, flags, rc): #Connexion au broker. client : client MQTT; userdata: données optionnelles; flags: infos protocole et rc: return code
    if rc == 0:
        print("Connecté au broker MQTT")
        client.subscribe("meteo/topic") # on s'abonne à tout les topics
    else:
        print("Erreur de connexion :", rc)

def on_message(client, userdata, msg): #Reception d'un message
    print(f"Message reçu sur {msg.topic}")
    try:
        data = json.loads(msg.payload.decode()) #on charge et décode le contenu du message
        # On récupère les données météo envoyées par l'esp
        temperature = data.get("temperature")
        humidite = data.get("humidite")
        """DonneeMeteo.objects.create( # On les stocks
            temperature=temperature,
            humidite=humidite
        )
        print("Données sauvegardées")""" #pour sauvergarder les données dans la base de donnée
    except Exception as e:
        print("Erreur traitement message :", e)

# Creartion du clien mqtt
def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60) # connexion du clien en local sur le port 1883
    client.loop_start()


