# autenticacion/views.py

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.core.mail import send_mail
import random

from autenticacion.models import Usuario_Registro

class VRegistro(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form": form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()

            # Generar y enviar el código de verificación
            verification_code = random.randint(100000, 999999)
            request.session['verification_code'] = verification_code
            request.session['user_email'] = usuario.email

            # Enviar correo electrónico de verificación
            send_mail(
                'Código de Verificación',
                f'Tu código de verificación es: {verification_code}',
                'tu_correo@gmail.com',
                [usuario.email],
                fail_silently=False,
            )

            messages.success(request, 'Te hemos enviado un correo con un código de verificación. Verifícalo para completar el registro.')
            return redirect('verificar_codigo')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, "registro/registro.html", {"form": form})

class VVerificacion(View):
    def get(self, request):
        return render(request, "registro/verificar_codigo.html")

    def post(self, request):
        codigo_ingresado = request.POST.get("codigo")

        if codigo_ingresado == str(request.session.get('verification_code')):
            usuario_email = request.session.get('user_email')
            try:
                usuario = Usuario_Registro.objects.get(email=usuario_email)
                usuario.is_verified = True  # Asegúrate de que este campo exista en tu modelo
                usuario.save()

                messages.success(request, 'Tu cuenta ha sido verificada. Ahora puedes iniciar sesión.')
                return redirect('logear')
            except Usuario_Registro.DoesNotExist:
                messages.error(request, 'No se encontró un usuario con ese correo electrónico.')
        else:
            messages.error(request, 'Código de verificación incorrecto. Intenta de nuevo.')

        return render(request, "registro/verificar_codigo.html")

def logear(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            rut_usu = form.cleaned_data.get("rut")

            # Buscar el usuario por el nombre de usuario y el RUT
            try:
                usuario = Usuario_Registro.objects.get(username=nombre_usuario, rut=rut_usu)
            except Usuario_Registro.DoesNotExist:
                usuario = None

            # Si el usuario existe y la contraseña es correcta
            if usuario is not None:
                usuario_autenticado = authenticate(username=nombre_usuario, password=contra)
                if usuario_autenticado is not None:
                    login(request, usuario_autenticado)
                    usuario.is_online = True
                    usuario.save()
                    return redirect('Index')
                else:
                    messages.error(request, "Contraseña incorrecta.")
            else:
                messages.error(request, "Usuario o RUT no válido.")
        else:
            messages.error(request, "Información incorrecta.")

    form = CustomAuthenticationForm()
    return render(request, "login/login.html", {"form": form})

def cerrar_sesion(request):
    usuario = request.user
    usuario.is_online = False
    usuario.save()
    logout(request)
    return redirect('Index')
