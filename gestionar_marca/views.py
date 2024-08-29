from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Marca
from .forms import MarcaForm

def dashboard(request): 
    return render(request, 'dashboard.html')

@login_required
def editar_marca(request, marca_id):
    # Buscar la marca usando filter y first en lugar de get_object_or_404
    marca = Marca.objects.filter(id=marca_id).first()
    
    if marca is None:
        # Si la marca no se encuentra, mostrar un mensaje de error y redirigir
        messages.error(request, 'Marca no encontrada.')
        return redirect('gestionar_marca')

    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca actualizada con éxito.')
            return redirect('gestionar_marca')
    else:
        form = MarcaForm(instance=marca)
    
    return render(request, 'editar_marca.html', {'form': form, 'marca': marca})

@login_required
def activar_inactivar_marca(request, marca_id):
    # Buscar la marca usando filter y first en lugar de get_object_or_404
    marca = Marca.objects.filter(id=marca_id).first()
    
    if marca is None:
        # Si la marca no se encuentra, mostrar un mensaje de error y redirigir
        messages.error(request, 'Marca no encontrada.')
        return redirect('gestionar_marca')

    # Cambiar el estado de la marca
    marca.estado = not marca.estado
    marca.save()
    estado = "activada" if marca.estado else "inactivada"
    messages.success(request, f'Marca {estado} con éxito.')
    return redirect('gestionar_marca')

@login_required
def consultar_marca(request):
    if request.method == 'POST':
        id_marca = request.POST.get('id_marca')
        nombre = request.POST.get('nombre')
        marca = None
        if id_marca:
            marca = Marca.objects.filter(id=id_marca).first()
        elif nombre:
            marca = Marca.objects.filter(nombre__icontains=nombre).first()
        if marca:
            return render(request, 'consultar_marca.html', {'marca': marca})
        else:
            messages.error(request, 'Marca no encontrada.')
    return render(request, 'consultar_marca.html')

@login_required
def gestionar_marca(request):
    marcas = Marca.objects.all()
    return render(request, 'gestionar_marca.html', {'marcas': marcas})

@login_required
def añadir_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca añadida con éxito.')
            return redirect('gestionar_marca')
    else:
        form = MarcaForm()
    return render(request, 'añadir_marca.html', {'form': form})

# Nota: Asegúrate de que estas vistas estén registradas en tu archivo urls.py
