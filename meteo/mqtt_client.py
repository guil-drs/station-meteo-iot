import paho.mqtt.client as mqtt #librairie mqtt
import json # pour lire les fichiers json envoyés par l'esp32
from django.conf import settings
from .models import DonneeMeteo # pour stocker les données recus de l'esp32


def on_connect(client, userdata, flags, rc): #Connexion au broker. client : client MQTT; userdata: données optionnelles; flags: infos protocole et rc: return code
    if rc == 0:
        print("Connecté au broker MQTT")
        client.subscribe("meteo/topic") # on s'abonne à tout les topics
    else:
        print("Erreur de connexion :", rc)

def on_message(client, userdata, msg):
    print(f"Message reçu sur {msg.topic}")
    try:
        data = json.loads(msg.payload.decode())

        temperature = data.get("temperature")
        pression = data.get("pression")
        altitude = data.get("altitude")

        DonneeMeteo.objects.create(
            temperature=temperature,
            pression=pression,
            altitude=altitude
        )

        print("Données sauvegardées")

    except Exception as e:
        print("Erreur traitement message :", e)

# Creartion du clien mqtt
def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60) # connexion du clien en local sur le port 1883
    client.loop_start()


