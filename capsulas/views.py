from django.shortcuts import render
from capsulas.models import Capsula

def capsulas(request):
    capsulas = Capsula.objects.all()
    return render(request, "capsulas/capsulas.html", {'capsulas': capsulas})