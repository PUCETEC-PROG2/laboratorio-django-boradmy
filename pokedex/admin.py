from django.contrib import admin
from .models import Pokemon
from .models import Entrenador_Pokemon
# Register your models here.

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

@admin.register(Entrenador_Pokemon)
class EntrenadorPokemonAdmin(admin.ModelAdmin):
    pass
    