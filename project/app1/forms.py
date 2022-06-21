from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

#from user.models import Avatar


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='username', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['email', 'username']
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


#class AvatarForm(ModelForm):
#    class Meta:
#        model = Avatar
#        fields = ('image', )