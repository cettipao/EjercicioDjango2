from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 40)

class Cliente(models.Model):
    nombre = models.CharField(max_length = 20)
    telefonos = models.ForeignKey(
        'Telefono',
        on_delete=models.CASCADE,
        null=False
    )

class Telefono(models.model):
    numero = models.CharField(max_length = 20)
    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
        null=False
    )
