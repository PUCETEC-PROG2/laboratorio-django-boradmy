from django.http import HttpResponse
from django.template import loader
from .models import Pokemon
from .models import Entrenador_Pokemon

from pokedex.forms import PokemonForm
from django.shortcuts import redirect, render

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

from django.shortcuts import render, redirect


def add_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
             
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    
    return render(request, 'pokemon_form.html', {'form': form}) 

    #editar pokemon
    
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
             
            return redirect('pokedex:index')
    else: 
        form = PokemonForm(instance=pokemon)
    
    return render(request, 'pokemon_form.html', {'form': form}) 

def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')
    