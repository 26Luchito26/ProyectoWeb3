from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserCreationForm
from .models import Usuario_Registro

# Definición del formulario para editar usuarios
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario_Registro
        fields = ['username', 'first_name', 'last_name', 'email', 'tipo_usuario', 'rut', 'is_staff', 'is_superuser']

# Definición del administrador personalizado de usuarios
class CustomUserAdmin(BaseUserAdmin):
    # Formulario para añadir nuevos usuarios
    add_form = CustomUserCreationForm
    
    # Formulario para cambiar detalles de usuarios existentes
    form = CustomUserChangeForm
    
    # Modelo que estamos registrando
    model = Usuario_Registro
    
    # Campos a mostrar en la lista de usuarios en el admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'tipo_usuario', 'is_staff', 'is_superuser', 'rut')
    
    # Campos por los que se puede buscar
    search_fields = ('username', 'email', 'rut')  # Buscar también por RUT
    
    # Ordenación por defecto
    ordering = ('username',)

    # Definir los grupos de campos a mostrar cuando se visualiza o edita un usuario
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'tipo_usuario', 'rut')}),
        ('Permisos', {'fields': ('is_staff', 'is_superuser')}),
    )

    # Definir los grupos de campos a mostrar cuando se añade un nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'tipo_usuario', 'rut', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )

    # Definir filtros laterales en la vista de lista
    list_filter = ('tipo_usuario', 'is_staff', 'is_superuser')

# Registrar el modelo en el admin
admin.site.register(Usuario_Registro, CustomUserAdmin)
