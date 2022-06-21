from django.urls import path
from app1.views import *

urlpatterns = [
    # path('', httpResponse, name='httpResponse'),
    path('',landing_page, name='landing_page'),
    path('main/', main_page, name='main_page'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
