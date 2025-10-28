from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import Entrenador_Pokemon

def index(request):
    pokemons = Pokemon.objects.all()
    entrenadores = Entrenador_Pokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons, 'entrenadores': entrenadores}, request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))


def entrenador(request, entrenador_id):
    entrenador = Entrenador_Pokemon.objects.get(id = entrenador_id)
    template = loader.get_template('display_entrenador.html')
    context = {
        'entrenador': entrenador
    }
    return HttpResponse(template.render(context, request))