from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import Usuario_Registro



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm 
    list_display = ('username', 'email', 'first_name', 'last_name', 'tipo_usuario', 'is_staff', 'is_superuser','rut')
    search_fields = ('username', 'email', 'rut')  # Incluir 'rut' en los campos de búsqueda si es necesario
    ordering = ('username',)

admin.site.register(Usuario_Registro, CustomUserAdmin)
