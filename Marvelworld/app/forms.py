from django import forms
from .models import Productos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('nombre', 'precio', 'descripcion', 'img')

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                "password1",
                "password2",
            ]
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
                "password1" : 'contraseña',
                "password2" : 'repetir contraseña'
        }