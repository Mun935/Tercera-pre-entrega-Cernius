from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})


def buscar_productos(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'productos_busqueda.html', {'resultados': resultados, 'termino_busqueda': termino_busqueda})
    else:
        form = BusquedaForm()
    return render(request, 'buscar_productos.html', {'form': form})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})
