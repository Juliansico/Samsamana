from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import  Categoria
from .forms import  CategoriaForm

# Create your views here.

@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')
@never_cache
@login_required
def gestionar_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestionar_categoria.html', {'categorias': categorias})


@never_cache
@login_required
def añadir_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría añadida con éxito.')
            return redirect('gestionar_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'añadir_categoria.html', {'form': form})


@never_cache
@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada con éxito.')
            return redirect('gestionar_categoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form, 'categoria': categoria})


@never_cache
@login_required
def activar_inactivar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.estado = not categoria.estado
    categoria.save()
    estado = "activada" if categoria.estado else "inactivada"
    messages.success(request, f'Categoría {estado} con éxito.')
    return redirect('gestionar_categoria')

@never_cache
@login_required
def filtrar_categorias(request):
    estado_filtro = request.GET.get('estado', None)
    buscar = request.GET.get('buscar', '')

    categorias = Categoria.objects.all()

    if estado_filtro == 'activado':
        categorias = categorias.filter(estado=True)
    elif estado_filtro == 'inactivado':
        categorias = categorias.filter(estado=False)

    if buscar:
        categorias = categorias.filter(nombre__icontains=buscar)

    context = {
        'categorias': categorias,
    }

    return render(request, 'gestionar_categoria.html', context)
