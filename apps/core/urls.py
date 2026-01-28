from django.urls import path
from . import views # Importa as views da própria pasta core

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
]