from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.name
    
class Entrenador_Pokemon(models.Model):
    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    level = models.IntegerField()
    fechadenacimiento = models.DateField()

    def __str__(self):
        return self.name