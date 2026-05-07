from django.shortcuts import render
from .models import DonneeMeteo
from django.utils import timezone
from datetime import timedelta
import json
import zoneinfo

def page_demo(request):
    paris = zoneinfo.ZoneInfo("Europe/Paris")
    deux_jours_avant = timezone.now() - timedelta(days=2)
    toutes_les_mesures = DonneeMeteo.objects.filter(timestamp__gte=deux_jours_avant).order_by('timestamp')

    # 1 mesure toutes les 5 minutes
    mesures_filtrees = []
    dernier_timestamp = None
    for d in toutes_les_mesures:
        if dernier_timestamp is None or (d.timestamp - dernier_timestamp).seconds >= 300:
            mesures_filtrees.append(d)
            dernier_timestamp = d.timestamp

    mesures_list = []
    for d in mesures_filtrees:
        timestamp_paris = d.timestamp.astimezone(paris)
        mesures_list.append({
            "temperature": d.temperature,
            "pression": d.pression,
            "altitude": d.altitude,
            "timestamp": timestamp_paris.strftime("%d/%m %H:%M")
        })

    mesures_json = json.dumps(mesures_list)

    return render(request, "meteo/demo-Copie.html", {
        "mesures_json": mesures_json
    })