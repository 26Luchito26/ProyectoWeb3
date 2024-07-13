from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required  # Importar el decorador
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm

class VRegistro(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form": form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Index')  
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, "registro/registro.html", {"form": form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Index')  # Redirige a la página principal después de cerrar sesión

def logear(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            rut_usu = form.cleaned_data.get("rut")
            usuario = authenticate(username=nombre_usuario, password=contra, rut=rut_usu)
            if usuario is not None:
                login(request, usuario)
                return redirect('Index')  # Redirige a la página principal después de iniciar sesión
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")

    form = CustomAuthenticationForm()
    return render(request, "login/login.html", {"form": form})