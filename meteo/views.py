from django.shortcuts import render
from .models import DonneeMeteo
import json

def page_demo(request):
    mesures = DonneeMeteo.objects.order_by('-timestamp')[:20][::-1]

    mesures_list = []
    for d in mesures:
        mesures_list.append({
            "temperature": d.temperature,
            "pression": d.pression,
            "altitude": d.altitude,
            "timestamp": d.timestamp.strftime("%H:%M:%S")
        })

    mesures_json = json.dumps(mesures_list)

    return render(request, "meteo/demo-Copie.html", {
        "mesures_json": mesures_json
    })