from django.urls import path
from . import views

app_name = "pokedex"

urlpatterns = [
    path("", views.index, name="index"),
    # Ruta directa
    path("<int:pokemon_id>/", views.pokemon, name="pokemon_directo"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
]