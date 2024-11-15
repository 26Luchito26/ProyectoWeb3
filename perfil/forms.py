from django import forms
from .models import Perfil
from autenticacion.models import Usuario_Registro

class PerfilForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(disabled=True)
    rut = forms.CharField(disabled=True)
    tipo_usuario = forms.CharField(disabled=True)
    
    class Meta:
        model = Perfil
        fields = ['imagen', 'biografia', 'telefono', 'direccion', 'cargo', 'departamento',
                 'emergencia_nombre', 'emergencia_parentesco', 'emergencia_telefono', 'emergencia_direccion']
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.usuario:
            self.fields['username'].initial = self.instance.usuario.username
            self.fields['first_name'].initial = self.instance.usuario.first_name
            self.fields['last_name'].initial = self.instance.usuario.last_name
            self.fields['email'].initial = self.instance.usuario.email
            self.fields['rut'].initial = self.instance.usuario.rut
            self.fields['tipo_usuario'].initial = self.instance.usuario.tipo_usuario 