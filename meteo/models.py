from django.db import models #models sert à créer des bases de données

class DonneeMeteo(models.Model):
    temperature = models.FloatField()
    humidite = models.FloatField()
    pression = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - Température:{self.temperature}°C Humidité:{self.humidite}% Pression:{self.humidite}hPa"