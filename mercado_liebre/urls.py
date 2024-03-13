from django.contrib import admin
from django.urls import path
from mercado_liebre.views import *

urlpatterns = [
    path("", home, name='home'),
    path("buscar/", buscar_productos, name='buscar_productos'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('categorias/', categorias, name='categorias'),
]