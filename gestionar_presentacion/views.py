from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Presentacion
from .forms import PresentacionForm
from django.views.decorators.cache import never_cache

@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')


@never_cache
@login_required

def gestionar_presentacion(request):
    presentaciones = Presentacion.objects.all()
    if request.method == 'POST':
        form = PresentacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Presentación creada con éxito.')
            return redirect('gestionar_presentacion')
    else:
        form = PresentacionForm()
    return render(request, 'gestionar_presentacion.html', {'presentaciones': presentaciones, 'form': form})


@never_cache
@login_required
def añadir_presentacion(request):
    if request.method == 'POST':
        form = PresentacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Presentación añadida con éxito.')
            return redirect('gestionar_presentacion')
    else:
        form = PresentacionForm()
    return render(request, 'añadir_presentacion.html', {'form': form})


@login_required
def editar_presentacion(request, presentacion_id):
    presentacion = get_object_or_404(Presentacion, id=presentacion_id)
    if request.method == 'POST':
        form = PresentacionForm(request.POST, instance=presentacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Presentación actualizada con éxito.')
            return redirect('gestionar_presentacion')
    else:
        form = PresentacionForm(instance=presentacion)
    return render(request, 'editar_presentacion.html', {'form': form, 'presentacion': presentacion})



@login_required
def activar_inactivar_presentacion(request, presentacion_id):
    presentacion = get_object_or_404(Presentacion, id=presentacion_id)
    presentacion.estado = not presentacion.estado
    presentacion.save()
    estado = "activada" if presentacion.estado else "inactivada"
    messages.success(request, f'Presentación {estado} con éxito.')
    return redirect('gestionar_presentacion')


@never_cache
@login_required
def filtrar_presentaciones(request):
    estado_filtro = request.GET.get('estado', None)
    buscar = request.GET.get('buscar', '')

    presentaciones = Presentacion.objects.all()

    if estado_filtro == 'activado':
        presentaciones = presentaciones.filter(estado=True)
    elif estado_filtro == 'inactivado':
        presentaciones = presentaciones.filter(estado=False)

    if buscar:
        presentaciones = presentaciones.filter(nombre__icontains=buscar)

    context = {
        'presentaciones': presentaciones,
    }

    return render(request, 'gestionar_presentacion.html', context)










# Create your views here.
