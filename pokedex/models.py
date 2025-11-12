from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    picture = models.ImageField(upload_to='pokemons/', null=True, blank=True)


    def __str__(self):
        return self.name
    
class Entrenador_Pokemon(models.Model): 
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pokemons = models.ManyToManyField(Pokemon)

    def __str__(self):
        return self.name
    

