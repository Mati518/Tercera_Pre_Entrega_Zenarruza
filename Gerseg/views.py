from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    return render(request, "Gerseg/inicio.html")

def barras(request):
    return render(request, "Gerseg/barras.html")

def discos(request):
    return render(request, "Gerseg/discos.html")

def bancas(request):
    return render(request, "Gerseg/bancas.html")

def racks(request):
    return render(request, "Gerseg/racks.html")

def fBancas(request):
    if request.method == "POST":
        formulario1 = FBancas(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            bancas = Bancas(medidas=info["medidas"], regulable=info["regulable"], materialRecubrimiento=info["materialRecubrimiento"], marca=info["marca"])
            bancas.save()
            return render(request, "Gerseg/inicio.html")
        
    else:
        formulario1 = FBancas()

    return render(request, "Gerseg/F/fBancas.html", {"form1": formulario1})

def fBarras(request):
    if request.method == "POST":
        formulario2 = FBarras(request.POST)
        if formulario2.is_valid():
            info2 = formulario2.cleaned_data
            barras = Barras(medidas=info2["medidas"], peso=info2["peso"], tipo=info2["tipo"], marca=info2["marca"], modelo=info2["modelo"])
            barras.save()
            return render(request, "Gerseg/inicio.html")
        
    else:
        formulario2 = FBarras()

    return render(request, "Gerseg/F/fBarras.html", {"form2": formulario2})

def fCliente(request):
    if request.method == "POST":
        formulario3 = FCliente(request.POST)
        if formulario3.is_valid():
            info3 = formulario3.cleaned_data
            cliente = Cliente(nombre=info3["nombre"], apellido=info3["apellido"], nUsuario=info3["nUsuario"], email=info3["email"], edad=info3["edad"], direccion=info3["direccion"])
            cliente.save()
            return render(request, "Gerseg/inicio.html")
        
    else:
        formulario3 = FCliente()

    return render(request, "Gerseg/F/fCliente.html", {"form3": formulario3})

def fDiscos(request):
    if request.method == "POST":
        formulario4 = FDiscos(request.POST)
        if formulario4.is_valid():
            info4 = formulario4.cleaned_data
            discos = Discos(medidas=info4["medidas"], peso=info4["peso"], tipo=info4["tipo"], marca=info4["marca"])
            discos.save()
            return render(request, "Gerseg/inicio.html")
        
    else:
        formulario4 = FDiscos()

    return render(request, "Gerseg/F/fDiscos.html", {"form4": formulario4})

def fRacks(request):
    if request.method == "POST":
        formulario5 = FRacks(request.POST)
        if formulario5.is_valid():
            info5 = formulario5.cleaned_data
            racks = Racks(medidas=info5["medidas"], peso=info5["peso"], marca=info5["marca"])
            racks.save()
            return render(request, "Gerseg/inicio.html")
        
    else:
        formulario5 = FRacks()

    return render(request, "Gerseg/F/fRacks.html", {"form5": formulario5})

def sBancas(request):
     return render(request, "Gerseg/bancas.html")

def resultadosBancas(request):
     if request.GET["marca"]:
          marca = request.GET["marca"]
          medidas = Bancas.objects.filter(marca__icontains = marca)
          return render(request, "Gerseg/bancas.html", {"marca":marca , "medidas":medidas })
     else:

          respuesta = "no enviaste datos."
    
     return HttpResponse(respuesta)

def sBarras(request):
     return render(request, "Gerseg/barras.html")

def resultadosBarras(request):
     if request.GET["marca"]:
          marca = request.GET["marca"]
          medidas = Barras.objects.filter(marca__icontains = marca)
          return render(request, "Gerseg/barras.html", {"marca":marca , "medidas":medidas })
     else:

          respuesta = "no enviaste datos."
    
     return HttpResponse(respuesta)

def sDiscos(request):
     return render(request, "Gerseg/discos.html")

def resultadosDiscos(request):
     if request.GET["marca"]:
          marca = request.GET["marca"]
          medidas = Discos.objects.filter(marca__icontains = marca)
          return render(request, "Gerseg/discos.html", {"marca":marca , "medidas":medidas })
     else:

          respuesta = "no enviaste datos."
    
     return HttpResponse(respuesta)

def sRacks(request):
     return render(request, "Gerseg/racks.html")

def resultadosRacks(request):
     if request.GET["marca"]:
          marca = request.GET["marca"]
          medidas = Racks.objects.filter(marca__icontains = marca)
          return render(request, "Gerseg/racks.html", {"marca":marca , "medidas":medidas })
     else:

          respuesta = "no enviaste datos."
    
     return HttpResponse(respuesta)