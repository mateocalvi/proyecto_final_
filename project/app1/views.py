from multiprocessing import context
from django.shortcuts import render


import os
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render


from app1.forms import UserEditForm, AvatarForm, SignUpForm
from app1.models import Avatar, Usuario


# Create your views here.

from django.http import HttpResponse

# def httpResponse(request):
    # return HttpResponse("Hello, world. You're at the app1 index.")

def landing_page(request):
    return render(request, 'landing_page.html')

def main_page(request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.all()
        context = {'usuario': usuario}
        return render(request, 'films_page.html', context)

    return render(request, 'films_page.html')

def sign_in(request):
    return render(request, 'forms\\login\\sign_in.html')

def login(request):
    return render(request, 'forms\\login\\login.html')

# TODO hacer una función que me permita desloguearse

def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        form.save()
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            return redirect('main_page')
    else:
        form = SignUpForm()
        return redirect('main_page')

    context = {'form': form}
    
    return render(request, 'forms\\login\\sign_in.html', context)


# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("home:main")

#         return render(
#             request=request,
#             context={'form': form},
#             template_name="login/login.html",
#         )

#     form = AuthenticationForm()
#     return render(
#         request=request,
#         context={'form': form},
#         template_name="login/login.html",
#     )