from django.shortcuts import render


import os
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render


from app1.forms import UserRegisterForm, UserEditForm, AvatarForm
from app1.models import Avatar


# Create your views here.

from django.http import HttpResponse

# def httpResponse(request):
    # return HttpResponse("Hello, world. You're at the app1 index.")

def landing_page(request):
    return render(request, 'landing_page.html')

def main_page(request):
    return render(request, 'films_page.html')

def sign_in(request):
    return render(request, 'forms\\login\\sign_in.html')

def login(request):
    return render(request, 'forms\\login\\login.html')




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("user:user-login")
    form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="user/register.html",
    )


def login_request(request): ##Validación de datos ingresados, para saber si mantengo sesion iniciada .
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home:main")    #Si los datos ingresados son correctos, voy al main.

        return render(
            request=request,
            context={'form': form},
            template_name="user/login.html",       
        )

    form = AuthenticationForm()     #Si los datos ingresados están mal, return nuevamente al login-
    return render(
        request=request,
        context={'form': form},
        template_name="user/login.html",
    )


def logout_request(request):  ##Cerrar sesión del usuario activo
      logout(request)
      return redirect("user:user-login")
