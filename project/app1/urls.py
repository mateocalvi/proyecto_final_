from django.urls import path
from app1.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # access url's
    path("login", auth_views.LoginView.as_view(), name="login"),
    
    # app url's
    path('',landing_page, name='landing_page'),
    path('main/', main, name='main'),
    path('signup/', signup, name='signup'),
    # path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    
]
