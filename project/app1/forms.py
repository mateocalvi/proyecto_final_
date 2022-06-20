from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from app1.models import Avatar

class UserRegisterForm(UserCreationForm):
    nombre = forms.CharField(label='Nombre', min_length=2)
    apellido = forms.CharField(label="Apellido", min_length=2)
    email = forms.EmailField(label='Correo electrónico')
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    contrasena2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)


class UserEditForm(UserChangeForm):
    contrasena = None

    class Meta:
        model = User
        fields = ['email', ] # 'nombre', 'apellido'
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
            # 'nombre' : forms.TextInput(attrs={'readonly': 'readonly'}),
            # 'apellido': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )