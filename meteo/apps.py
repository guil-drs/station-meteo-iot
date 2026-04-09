from django.apps import AppConfig


class MeteoConfig(AppConfig): #configuration de l'app meteo
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meteo'

    def ready(self): #fonction quand Django démarre
        import os #on met les imports dans class pr eviter des erreurs d'import
        if os.environ.get('RUN_MAIN') != 'true': # permet de ne pas lancer le MQTT deux fois quand on lance le serveur
            return

        from .mqtt_client import start_mqtt
        start_mqtt() #lance le client mqtt
        