from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario_Registro(AbstractUser):
    TIPO_USUARIO_TRABAJADOR = 'Trabajador'
    TIPO_USUARIO_JEFE = 'Jefe'
    TIPO_USUARIO_ADMINISTRADOR = 'Administrador Informático' # Se encarga del administrar todos los sistemas
    TIPO_USUARIO_ADMINISTRADOR_OPERACIONAL = 'Administrador Operacional'  # Puede gestionar todas las solicitudes y recuperar las borradas

    TIPO_USUARIO_CHOICES = [
        (TIPO_USUARIO_TRABAJADOR, 'Trabajador'),
        (TIPO_USUARIO_JEFE, 'Jefe'),
        (TIPO_USUARIO_ADMINISTRADOR, 'Administrador Informático'),
        (TIPO_USUARIO_ADMINISTRADOR_OPERACIONAL, 'Administrativo Operacional'),  
    ]

    tipo_usuario = models.CharField(max_length=30, choices=TIPO_USUARIO_CHOICES, default=TIPO_USUARIO_TRABAJADOR)
    rut = models.CharField(max_length=12, unique=True, blank=True)
    is_online = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.tipo_usuario == self.TIPO_USUARIO_ADMINISTRADOR:
            self.is_staff = True
            self.is_superuser = True
        elif self.tipo_usuario == self.TIPO_USUARIO_ADMINISTRADOR_OPERACIONAL:
            self.is_staff = True  # El administrador operacional es staff pero no superusuario
            self.is_superuser = False
        else:
            self.is_staff = False
            self.is_superuser = False

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
