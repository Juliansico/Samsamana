from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import  get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from django.contrib import messages
from .models import Venta
from .forms import VentaForm

@login_required
def gestionar_ventas(request):
    ventas = Venta.objects.all()
    total_venta_realizada = Venta.objects.aggregate(Sum('cantidad_Venta'))['cantidad_Venta__sum']
    ventas_activas = Venta.objects.filter(estado=True)
    ventas_inactivas = Venta.objects.filter(estado=False)

    context = {
        'ventas': ventas,
        'total_venta_realizada': total_venta_realizada,
        'ventas_activas': ventas_activas,
        'ventas_inactivas': ventas_inactivas,
    }

    return render(request, 'gestionar_ventas.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def editar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta actualizada con éxito.')
            return redirect('gestionar_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'editar_venta.html', {'form': form, 'venta': venta})


@login_required
def consultar_venta(request):
    if request.method == 'POST':
        id_venta = request.POST.get('id_venta')
        ventas = Venta.objects.filter(id=id_venta)
        return render(request, 'consultar_venta.html', {'ventas': ventas})
    return render(request, 'consultar_venta.html')


@login_required
def añadir_venta(request):
    Usuario = get_user_model()
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.id_Usuario = Usuario.objects.get(id=request.user.id)
            venta.total_Venta_Realizada = venta.precio_Producto * venta.cantidad_Venta
            venta.save()
            messages.success(request, 'Venta añadida con éxito.')
            return redirect('gestionar_ventas')
    else:
        form = VentaForm()
    return render(request, 'añadir_venta.html', {'form': form})

@login_required
def activar_desactivar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id, id_Usuario=request.user)
    venta.estado = not venta.estado
    estado = "activada" if venta.estado else "inactivada" 
    messages.success(request, f'Venta {estado} con éxito.')
    venta.save()
    return redirect('gestionar_ventas')


