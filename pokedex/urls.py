from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("entrenador/<int:entrenador_id>/", views.entrenador, name="entrenador"),
]