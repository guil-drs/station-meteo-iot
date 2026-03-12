from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('demo/', views.page_demo, name='demo'),  # URL: /meteo/demo/
    path("admin/", admin.site.urls), # configuration d'URL prédéfinie fournie par Django pour le site d'administration par défaut
]
