from django.shortcuts import render
import random, json
from datetime import datetime, timedelta

def page_demo(request):
    # Simuler les 10 dernières mesures
    mesures = []
    now = datetime.now()
    for i in range(10):
        mesures.append({
            "date": (now - timedelta(minutes=i*5)).strftime("%H:%M"),
            "temperature": round(random.uniform(15, 25), 1),
            "humidite": round(random.uniform(40, 80), 1),
            "pression": round(random.uniform(1000, 1020), 1)
        })
    # Convertir en JSON pour JS
    mesures_json = json.dumps(mesures)
    return render(request, "meteo/demo.html", {"mesures_json": mesures_json})



    
