from django import forms
from .models import Solicitudes_Epps, Solicitudes_Retiro, Solicitudes_Tolva

class SolicitudEppsForm(forms.ModelForm):
    class Meta:
        model = Solicitudes_Epps
        fields = ['nombreEpps', 'fecha_realizarEP', 'descripcionEpps', 'tipo_materialEpps']
        widgets = {
            'fecha_realizarEP': forms.DateInput(attrs={'type': 'date'})
        }

class SolicitudRetiroForm(forms.ModelForm):
    class Meta:
        model = Solicitudes_Retiro
        fields = ['nombre_retiro', 'fecha_realizarR', 'descripcionRetiro', 'cantidadRetiro', 'tipo_materialRetiro', 'patente']
        widgets = {
            'fecha_realizarR': forms.DateInput(attrs={'type': 'date'})
        }

class SolicitudTolvaForm(forms.ModelForm):
    class Meta:
        model = Solicitudes_Tolva
        fields = ['nombre_tolva', 'fecha_realizarT', 'descripcionTolva', 'tipo_retiro_pedido']
        widgets = {
            'fecha_realizarT': forms.DateInput(attrs={'type': 'date'})
        }
