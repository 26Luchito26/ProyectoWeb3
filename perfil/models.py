from django.db import models
from autenticacion.models import Usuario_Registro
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario_Registro, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='perfiles/', default='perfiles/default.png')
    biografia = models.TextField(max_length=500, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    cargo = models.CharField(max_length=100, blank=True)
    departamento = models.CharField(max_length=100, blank=True)
    
    # Nuevos campos para contacto de emergencia
    emergencia_nombre = models.CharField(max_length=100, blank=True, verbose_name="Nombre contacto de emergencia")
    emergencia_parentesco = models.CharField(max_length=50, blank=True, verbose_name="Parentesco")
    emergencia_telefono = models.CharField(max_length=15, blank=True, verbose_name="Teléfono de emergencia")
    emergencia_direccion = models.CharField(max_length=255, blank=True, verbose_name="Dirección contacto de emergencia")

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

@receiver(post_save, sender=Usuario_Registro)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
