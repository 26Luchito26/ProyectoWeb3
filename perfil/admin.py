from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Perfil
from autenticacion.models import Usuario_Registro

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'cargo', 'departamento')
    search_fields = ('usuario__username', 'telefono', 'cargo', 'departamento')
    list_filter = ('departamento',)
    fieldsets = (
        ('Usuario', {
            'fields': ('usuario', 'imagen', 'biografia', 'telefono', 'direccion', 'cargo', 'departamento')
        }),
        ('Contacto de Emergencia', {
            'fields': ('emergencia_nombre', 'emergencia_parentesco', 'emergencia_telefono', 'emergencia_direccion')
        }),
    )

admin.site.register(Perfil, PerfilAdmin)
