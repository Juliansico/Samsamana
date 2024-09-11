from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Usuario
from openpyxl.drawing.image import Image
import os
from .forms import UsuarioForm
from django.views.decorators.cache import never_cache
from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.utils import ImageReader
from django.conf import settings
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter


@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')

@never_cache
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

@never_cache
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
@never_cache
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

@never_cache
@login_required
@user_passes_test(lambda u: u.is_superuser)
def activar_inactivar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.estado = not usuario.estado
    usuario.save()
    estado = "activado" if usuario.estado else "inactivado"
    messages.success(request, f'Usuario {estado} con éxito.')
    return redirect('gestionar_usuarios')

@never_cache
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

def reporte_usuarios_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    margin = 50
    row_height = 20
    y_position = height - margin

    # Cargar la imagen de marca de agua
    watermark_path = os.path.join(settings.STATIC_ROOT, 'img', 'Samsamanalogo1PNG.png')
    if os.path.exists(watermark_path):
        try:
            p.saveState()
            p.setFillAlpha(0.5)  # Ajustar la transparencia
            img = ImageReader(watermark_path)
            iw, ih = img.getSize()
            aspect = ih / float(iw)
            p.drawImage(img, x=0, y=0, width=width, height=height * aspect, mask='auto', preserveAspectRatio=True)
            p.restoreState()
        except Exception as e:
            print("Error al agregar la marca de agua:", e)

    # Añadir títulos
    p.setFont("Helvetica-Bold", 24)
    p.drawString(margin, y_position, "SAMSAMANA")
    y_position -= 30
    p.setFont("Helvetica", 18)
    p.drawString(margin, y_position, "Reporte de Usuarios")
    y_position -= 50

    # Crear tabla con datos de usuarios
    column_widths = [50, 150, 100, 200, 100]
    headers = ["ID", "Usuario", "Apellido", "Teléfono", "Estado"]
    data = [headers]

    usuarios = Usuario.objects.all()
    for usuario in usuarios:
        data.append([
            str(usuario.id),
            usuario.username,
            usuario.apellido,
            usuario.telefono,
            'Activo' if usuario.estado else 'Inactivo'
        ])

    table = Table(data, colWidths=column_widths)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#25b6e6'),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 10),
        ('BACKGROUND', (0, 1), (-1, -1), '#f2f2f2'),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER')
    ])
    table.setStyle(style)
    
    # Ajustar la posición de la tabla
    table_width = sum(column_widths)
    table_x = (width - table_width - 2 * margin) / 2 + margin
    table_y = y_position - len(data) * row_height
    table.wrapOn(p, table_width, height - 2 * margin)
    table.drawOn(p, table_x, table_y)

    p.showPage()
    p.save()
    buffer.seek(0)

    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_usuarios.pdf"'
    return response

def reporte_usuarios_excel(request):
    # Crear un archivo Excel en memoria
    buffer = BytesIO()
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte de Usuarios"

    # Definir estilos
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="25b6e6", end_color="25b6e6", fill_type="solid")
    alignment_center = Alignment(horizontal="center", vertical="center")

    # Añadir logo (más pequeño) en la celda A1
    logo_path = os.path.join(settings.STATIC_ROOT, 'img', 'Samsamanalogo1PNG.png')
    if os.path.exists(logo_path):
        img = Image(logo_path)
        img.width = 80  # Ajustar tamaño según necesidad
        img.height = 40
        ws.add_image(img, 'A1')

    # Añadir título
    ws.merge_cells('B1:F1')
    title_cell = ws['B1']
    title_cell.value = "TABLA USUARIOS - BALNEARIO SAMSAMANA"
    title_cell.font = Font(bold=True, size=16)
    title_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Añadir encabezados
    headers = ["ID", "Usuario", "Apellido", "Teléfono", "Estado"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=2, column=col_num, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = alignment_center

    # Añadir datos de usuarios
    usuarios = Usuario.objects.all()
    for row_num, usuario in enumerate(usuarios, 3):
        ws.cell(row=row_num, column=1, value=usuario.id).alignment = alignment_center
        ws.cell(row=row_num, column=2, value=usuario.username).alignment = alignment_center
        ws.cell(row=row_num, column=3, value=usuario.apellido).alignment = alignment_center
        ws.cell(row=row_num, column=4, value=usuario.telefono).alignment = alignment_center
        ws.cell(row=row_num, column=5, value='Activo' if usuario.estado else 'Inactivo').alignment = alignment_center

    # Ajustar el ancho de las columnas
    column_widths = [10, 20, 20, 20, 15]  # Ajusta los anchos según sea necesario
    for col_num, width in enumerate(column_widths, 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = width

    # Guardar el archivo en el buffer
    wb.save(buffer)
    buffer.seek(0)

    # Preparar la respuesta HTTP
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Reporte_usuarios.xlsx"'
    return response
