from django import forms

class FCliente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=60)
    nUsuario = forms.CharField(max_length=60)
    email = forms.EmailField()
    edad = forms.IntegerField()
    direccion = forms.CharField(max_length=60)

class FBarras(forms.Form):
    medidas = forms.IntegerField()
    peso = forms.IntegerField()
    tipo = forms.CharField(max_length=60)
    marca = forms.CharField(max_length=60)
    modelo = forms.IntegerField()

class FDiscos(forms.Form):
    medidas = forms.IntegerField()
    tipo = forms.CharField(max_length=60)
    peso = forms.IntegerField()
    marca = forms.CharField(max_length=60)

class FRacks(forms.Form):
    medidas = forms.IntegerField()
    peso = forms.IntegerField()
    marca = forms.CharField(max_length=60)

class FBancas(forms.Form):
    medidas = forms.IntegerField()
    regulable = forms.BooleanField()
    materialRecubrimiento = forms.CharField(max_length=60)
    marca = forms.CharField(max_length=60)