from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.page_demo, name='demo'),  # URL: /meteo/demo/
]
