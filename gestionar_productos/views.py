from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
from gestionar_categoria.models import Categoria
from gestionar_marca.models import Marca
from gestionar_presentacion.models import Presentacion
import logging
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')
@never_cache
@login_required
def gestionar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestionar_productos.html', {'productos': productos})

@never_cache
@login_required
def añadir_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto añadido con éxito.')
            return redirect('gestionar_productos')
    else:
        form = ProductoForm()
    return render(request, 'añadir_producto.html', {'form': form})

@never_cache
@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado con éxito.')
            return redirect('gestionar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

@never_cache
@login_required
def filtrar_productos(request):
    estado_filtro = request.GET.get('estado', None)
    buscar = request.GET.get('buscar', '')
    precio_min = request.GET.get('precio_min', None)
    precio_max = request.GET.get('precio_max', None)
    categoria_id = request.GET.get('categoria', '')
    marca_id = request.GET.get('marca', '')
    presentacion_id = request.GET.get('presentacion', '')

    productos = Producto.objects.all()

    if estado_filtro == 'activado':
        productos = productos.filter(estado=True)
    elif estado_filtro == 'inactivado':
        productos = productos.filter(estado=False)

    if buscar:
        productos = productos.filter(nombre__icontains=buscar)
    if precio_min:
        productos = productos.filter(precio__gte=precio_min)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    if marca_id:
        productos = productos.filter(marca_id=marca_id)
    if presentacion_id:
        productos = productos.filter(presentacion_id=presentacion_id)
    

    context = {
        'productos': productos,
        'categorias': Categoria.objects.all(),
        'marcas': Marca.objects.all(),
        'presentaciones': Presentacion.objects.all(),
    }

    return render(request, 'gestionar_productos.html', context)
@never_cache
@login_required
def activar_inactivar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.estado = not producto.estado
    producto.save()
    estado = "activado" if producto.estado else "inactivado"
    messages.success(request, f'Producto {estado} con éxito.')
    return redirect('gestionar_productos')


