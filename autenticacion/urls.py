#urls.py
from django.urls import path
from django.contrib import admin
from .views import VVerificacion, cerrar_sesion, logear, VRegistro

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('verificar_codigo/', VVerificacion.as_view(), name="verificar_codigo"),  # Nueva ruta para la verificación
    path('logear/', logear, name="logear"),
]