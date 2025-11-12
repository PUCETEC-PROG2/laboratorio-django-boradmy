from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Ruta directa
    path("<int:pokemon_id>/", views.pokemon, name="pokemon_directo"),
]
