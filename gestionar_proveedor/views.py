from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Proveedor
from .forms import ProveedorForm
from django.views.decorators.cache import never_cache
from io import BytesIO
from openpyxl.drawing.image import Image
from django.http import HttpResponse
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import os


@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')
@never_cache
@login_required
def gestionar_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'gestionar_proveedor.html', {'proveedores': proveedores})
@never_cache
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


@never_cache
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


@never_cache
@login_required
def activar_inactivar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    proveedor.estado = not proveedor.estado
    proveedor.save()
    estado = "activado" if proveedor.estado else "inactivado"
    messages.success(request, f'Proveedor {estado} con éxito.')
    return redirect('gestionar_proveedor')


@never_cache
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

def reporte_proveedores_pdf(request):
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
    p.drawString(margin, y_position, "Reporte de Proveedores")
    y_position -= 50

    # Crear tabla con datos de proveedores
    column_widths = [50, 150, 100, 200, 100]
    headers = ["ID", "Nombre", "Teléfono", "Email", "Estado"]
    data = [headers]

    proveedores = Proveedor.objects.all()
    for proveedor in proveedores:
        data.append([
            str(proveedor.id),
            proveedor.nombre,
            proveedor.telefono,
            proveedor.email,
            'Activo' if proveedor.estado else 'Inactivo'
        ])

    table = Table(data, colWidths=column_widths)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#25b6e6'),
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
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
    response['Content-Disposition'] = 'attachment; filename="Reporte_proveedores.pdf"'
    return response

def reporte_proveedores_excel(request):
    # Crear un archivo Excel en memoria
    buffer = BytesIO()
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte de Proveedores"

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
    title_cell.value = "TABLA PROVEEDORES - BALNEARIO SAMSAMANA"
    title_cell.font = Font(bold=True, size=16)
    title_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Añadir encabezados
    headers = ["ID", "Nombre", "Teléfono", "Email", "Estado"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col_num, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = alignment_center

    # Añadir datos de proveedores
    proveedores = Proveedor.objects.all()
    for row_num, proveedor in enumerate(proveedores, 4):
        ws.cell(row=row_num, column=1, value=proveedor.id).alignment = alignment_center
        ws.cell(row=row_num, column=2, value=proveedor.nombre).alignment = alignment_center
        ws.cell(row=row_num, column=3, value=proveedor.telefono).alignment = alignment_center
        ws.cell(row=row_num, column=4, value=proveedor.email).alignment = alignment_center
        ws.cell(row=row_num, column=5, value='Activo' if proveedor.estado else 'Inactivo').alignment = alignment_center

    # Ajustar el ancho de las columnas
    column_widths = [10, 30, 20, 30, 15]  # Ajusta los anchos según sea necesario
    for col_num, width in enumerate(column_widths, 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = width

    # Guardar el archivo en el buffer
    wb.save(buffer)
    buffer.seek(0)

    # Preparar la respuesta HTTP
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Reporte_proveedores_samsamana.xlsx"'
    return response