from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=60)
    nUsuario = models.CharField(max_length=60)
    email = models.EmailField()
    edad = models.IntegerField()
    direccion = models.CharField(max_length=60)

class Barras(models.Model):
    medidas = models.IntegerField()
    peso = models.IntegerField()
    tipo = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    modelo = models.IntegerField()

class Discos(models.Model):
    medidas = models.IntegerField()
    tipo = models.CharField(max_length=60)
    peso = models.IntegerField()
    marca = models.CharField(max_length=60)

class Racks(models.Model):
    medidas = models.IntegerField()
    peso = models.IntegerField()
    marca = models.CharField(max_length=60)

class Bancas(models.Model):
    medidas = models.IntegerField()
    regulable = models.BooleanField()
    materialRecubrimiento = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)