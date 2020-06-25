from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 40)

class Telefono(models.model):
    numero = models.CharField(max_length = 20)
    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
        null=False
    )

class Ciudad(models.Model):
    nombre = models.CharField(max_length = 20)
class Comuna(models.Model):
    nombre = models.CharField(max_length = 20)
    ciudad = models.ForeignKey(
        'Ciudad',
        on_delete=models.CASCADE,
        null=False
    )

class Direccion(models.Model):
    numero = models.CharField(max_length = 5)
    calle = models.CharField(max_length = 20) 
    comuna = models.ForeignKey(
        'Comuna',
        on_delete=models.CASCADE,
        null=False
    )

class Cliente(models.Model):
    rut = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 20)
    direccion = models.ForeignKey(
        'Direccion',
        on_delete=models.CASCADE,
        null=False
    )

