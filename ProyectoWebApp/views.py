from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "ProyectoWebApp/index.html")

def bloqueado(request):
    return render(request, "ProyectoWebApp/bloqueado.html")



