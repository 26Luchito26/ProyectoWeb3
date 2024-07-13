from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario_Registro(AbstractUser):
    TIPO_USUARIO_TRABAJADOR = 'Trabajador'
    TIPO_USUARIO_JEFE = 'Jefe'
    TIPO_USUARIO_ADMINISTRADOR = 'Administrador'

    TIPO_USUARIO_CHOICES = [
        (TIPO_USUARIO_TRABAJADOR, 'Trabajador'),
        (TIPO_USUARIO_JEFE, 'Jefe'),
        (TIPO_USUARIO_ADMINISTRADOR, 'Administrador'),
    ]

    tipo_usuario = models.CharField(max_length=30, choices=TIPO_USUARIO_CHOICES, default=TIPO_USUARIO_TRABAJADOR)
    rut = models.CharField(max_length=12, unique=True, blank=True)  # Asegúrate de que el campo rut sea único


    def save(self, *args, **kwargs):
        if self.tipo_usuario == self.TIPO_USUARIO_ADMINISTRADOR:
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
