from django.urls import path
from .views import *

urlpatterns = [
    path('base/', base, name='base'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('header/', header, name='header'),
]
