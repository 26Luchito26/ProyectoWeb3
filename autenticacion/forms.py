
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario_Registro
from django.contrib.auth.forms import AuthenticationForm

def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "").lower()  # Limpiar formato
    if len(rut) < 2 or not rut[:-1].isdigit():
        return False  # Formato inválido
    
    verificador = rut[-1]
    rut = rut[:-1]
    suma = 0
    mul = 2
    
    for char in reversed(rut):
        suma += int(char) * mul
        mul += 1
        if mul > 7:
            mul = 2
    
    resto = suma % 11
    dv = 11 - resto
    
    if dv == 10:
        dv = "k"
    elif dv == 11:
        dv = "0"
    
    return str(dv) == verificador

class CustomAuthenticationForm(AuthenticationForm):
    rut = forms.CharField(label='RUT', max_length=12)

    class Meta(UserCreationForm.Meta):
        model = Usuario_Registro

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    rut = forms.CharField(label="Ingrese su RUT", max_length=12)

    class Meta(UserCreationForm.Meta):
        model = Usuario_Registro
        fields = ['username', 'first_name', 'last_name', 'email', 'tipo_usuario','rut']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def clean_rut(self):
        rut = self.cleaned_data.get("rut")
        if not validar_rut(rut):
            raise forms.ValidationError("El RUT ingresado no es válido.")
        if Usuario_Registro.objects.filter(rut=rut).exists():
            raise forms.ValidationError("El RUT ingresado ya está en uso.")
        return rut

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.rut = self.cleaned_data["rut"]  # Asignar el RUT al campo del modelo
        if commit:
            user.save()
        return user

