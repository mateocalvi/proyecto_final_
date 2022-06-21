from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from app1.models import Avatar, Usuario

# class UserRegisterForm(UserCreationForm):
#     nombre = forms.CharField(label='Nombre', min_length=2)
#     apellido = forms.CharField(label="Apellido", min_length=2)
#     email = forms.EmailField(label='Correo electrónico')
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', min_length=2)
    last_name = forms.CharField(label="Apellido", min_length=2)
    username = forms.CharField(label='Nombre de usuario', min_length=5, max_length=16)
    email = forms.EmailField(label='Correo electrónico')
    password1: forms.Field(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.Field(label='Repetir la contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username', 
            'email', 
            'password1', 
            'password2',
            ]


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