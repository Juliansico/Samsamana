from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Proveedor
from .forms import ProveedorForm

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def gestionar_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'gestionar_proveedor.html', {'proveedores': proveedores})

@login_required
def añadir_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor añadido con éxito.')
            return redirect('gestionar_proveedor')
    else:
        form = ProveedorForm()
    return render(request, 'añadir_proveedor.html', {'form': form})



@login_required
def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado con éxito.')
            return redirect('gestionar_proveedor')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor})



@login_required
def activar_inactivar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    proveedor.estado = not proveedor.estado
    proveedor.save()
    estado = "activado" if proveedor.estado else "inactivado"
    messages.success(request, f'Proveedor {estado} con éxito.')
    return redirect('gestionar_proveedor')



@login_required
def filtrar_proveedores(request):
    nombre_filtro = request.GET.get('nombre', '')
    estado_filtro = request.GET.get('estado', None)
    telefono_filtro = request.GET.get('telefono', '')
    email_filtro = request.GET.get('email', '')

    proveedores = Proveedor.objects.all()

    if nombre_filtro:
        proveedores = proveedores.filter(nombre__icontains=nombre_filtro)
    if estado_filtro == 'activado':
        proveedores = proveedores.filter(estado=True)
    elif estado_filtro == 'inactivado':
        proveedores = proveedores.filter(estado=False)
    if telefono_filtro:
        proveedores = proveedores.filter(telefono__icontains=telefono_filtro)
    if email_filtro:
        proveedores = proveedores.filter(email__icontains=email_filtro)

    context = {
        'proveedores': proveedores,
    }

    return render(request, 'gestionar_proveedor.html', context)

