from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Usuario
from .forms import UsuarioForm

def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def gestionar_usuarios(request):
    query = request.GET.get('q')
    if query:
        usuarios = Usuario.objects.filter(
            Q(usuario__icontains=query) |
            Q(apellido__icontains=query) |
            Q(documento__icontains=query)
        )
    else:
        usuarios = Usuario.objects.all()
    
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'gestionar_usuarios.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def añadir_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Remove any admin-related permissions
            usuario.user_permissions.clear()
            messages.success(request, 'Usuario añadido con éxito.')
            return redirect('gestionar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'añadir_usuario.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            if form.cleaned_data['password1']:
                usuario.set_password(form.cleaned_data['password1'])
            usuario.is_superuser = False  # Asegúrate de que no sea superusuario
            usuario.is_staff = True  # Si quieres que tenga acceso al admin
            usuario.save()
            rol_usuario = form.cleaned_data.get('rol_usuario')
            group = Group.objects.get(name=rol_usuario)
            usuario.groups.clear()
            usuario.groups.add(group)
            messages.success(request, 'Usuario actualizado con éxito.')
            return redirect('gestionar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def activar_inactivar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.estado = not usuario.estado
    usuario.save()
    estado = "activado" if usuario.estado else "inactivado"
    messages.success(request, f'Usuario {estado} con éxito.')
    return redirect('gestionar_usuarios')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def filtrar_usuarios(request):
    usuarios = Usuario.objects.all()

    nombre = request.GET.get('nombre')
    documento = request.GET.get('documento')
    telefono = request.GET.get('telefono')
    estado = request.GET.get('estado')

    if nombre:
        usuarios = usuarios.filter(username__icontains=nombre)
    if documento:
        usuarios = usuarios.filter(documento__icontains=documento)
    if telefono:
        usuarios = usuarios.filter(telefono__icontains=telefono)
    if estado:
        if estado == 'activado':
            usuarios = usuarios.filter(estado=True)
        elif estado == 'inactivado':
            usuarios = usuarios.filter(estado=False)

    return render(request, 'gestionar_usuarios.html', {'usuarios': usuarios})