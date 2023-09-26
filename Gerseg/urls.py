from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("barras/", barras, name="Barras"),
    path("discos/", discos, name="Discos"),
    path("bancas/", bancas, name="Bancas"),
    path("racks/", racks, name="Racks"),
    path("fBancas/", fBancas, name="fBancas"),
    path("fBarras/", fBarras, name="fBarras"),
    path("fCliente/", fCliente, name="fCliente"),
    path("fDiscos/", fDiscos, name="fDiscos"),
    path("fRacks/", fRacks, name="fRacks"),
    path("resultadosBancas", resultadosBancas, name="resultadoBancas"),
    path("resultadosBarras", resultadosBarras, name="resultadoBarras"),
    path("resultadosDiscos", resultadosDiscos, name="resultadoDiscos"),
    path("resultadosRacks", resultadosRacks, name="resultadoRacks"),
]