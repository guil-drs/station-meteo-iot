from django.shortcuts import render
from django.utils import timezone
from .models import DonneeMeteo
import json

def page_demo(request):
    # Récupérer les 20 dernières mesures
    mesures = DonneeMeteo.objects.order_by('-timestamp')[:20][::-1]

    # Convertir en dictionnaires simples
    mesures_list = []
    for d in mesures:
        mesures_list.append({
            "temperature": d.temperature,
            "humidite": d.humidite,
            "pression": d.pression,
            "timestamp": timezone.localtime(d.timestamp).strftime("%H:%M:%S")
        })

    # Convertir en JSON pour JS
    mesures_json = json.dumps(mesures_list)

    return render(request, "meteo/demo-Copie.html", {"mesures_json": mesures_json})