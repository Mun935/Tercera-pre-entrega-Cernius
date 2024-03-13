from django.contrib import admin
from django.urls import path
from mercado_liebre.views import *

urlpatterns = [
    path("", home, name='home'),
]