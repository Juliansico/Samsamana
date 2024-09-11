from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .models import Marca
from .forms import MarcaForm
from django.views.decorators.cache import never_cache
from io import BytesIO
from django.http import HttpResponse
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from .models import Marca
import os
from openpyxl.utils import get_column_letter
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.drawing.image import Image
@never_cache
def dashboard(request): 
    return render(request, 'dashboard.html')
@never_cache
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
@never_cache
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
@never_cache
@login_required
def filtrar_marcas(request):
    nombre_filtro = request.GET.get('buscar', '')
    estado_filtro = request.GET.get('estado', '')

    marcas = Marca.objects.all()

    if nombre_filtro:
        marcas = marcas.filter(nombre__icontains=nombre_filtro)

    if estado_filtro == 'activado':
        marcas = marcas.filter(estado=True)
    elif estado_filtro == 'inactivado':
        marcas = marcas.filter(estado=False)

    context = {
        'marcas': marcas
    }

    return render(request, 'gestionar_marca.html', context)
@never_cache
@login_required
def gestionar_marca(request):
    marcas = Marca.objects.all()
    return render(request, 'gestionar_marca.html', {'marcas': marcas})
@never_cache
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

def reporte_marcas_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    margin = 50
    table_width = width - 2 * margin
    row_height = 20
    y_position = height - margin

    # Cargar la imagen de marca de agua
    watermark_path = os.path.join(settings.STATIC_ROOT, 'img', 'Samsamanalogo1PNG.png')
    if os.path.exists(watermark_path):
        try:
            p.saveState()
            p.setFillAlpha(0.5)  # Ajusta la transparencia (0.1 = 10% opaco)
            img = ImageReader(watermark_path)
            iw, ih = img.getSize()
            aspect = ih / float(iw)
            p.drawImage(img, x=0, y=0, width=width, height=height*aspect, mask='auto', preserveAspectRatio=True)
            p.restoreState()
        except Exception as e:
            print("Error al agregar la marca de agua:", e)

    # Añadir títulos
    p.setFont("Helvetica-Bold", 24)
    p.drawString(margin, y_position, "SAMSAMANA")
    y_position -= 30
    p.setFont("Helvetica", 18)
    p.drawString(margin, y_position, "Reporte de Marcas")
    y_position -= 50

    # Crear tabla con datos de marcas
    column_widths = [50, 150, 60]
    headers = ["ID", "Nombre", "Estado"]
    data = [headers]

    marcas = Marca.objects.all()
    for marca in marcas:
        data.append([
            str(marca.id),
            marca.nombre,
            'Activo' if marca.estado else 'Inactivo'
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
    response['Content-Disposition'] = 'attachment; filename="Reporte_marcas.pdf"'
    return response

def reporte_marcas_excel(request):
    # Crear un archivo Excel en memoria
    buffer = BytesIO()
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte de Marcas"

    # Definir estilos
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="25b6e6", end_color="25b6e6", fill_type="solid")
    alignment_center = Alignment(horizontal="center", vertical="center")

    # Añadir logo (más pequeño)
    logo_path = os.path.join(settings.STATIC_ROOT, 'img', 'Samsamanalogo1PNG.png')
    if os.path.exists(logo_path):
        img = Image(logo_path)
        img.width = 80  # Ajustar el tamaño del logo
        img.height = 40
        ws.add_image(img, 'A1')

    # Añadir título
    ws.merge_cells('B1:E1')
    title_cell = ws['B1']
    title_cell.value = "TABLA MARCAS - BALNEARIO SAMSAMANA"
    title_cell.font = Font(bold=True, size=16)
    title_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Añadir encabezados
    headers = ["ID", "Nombre", "Estado"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col_num, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = alignment_center

    # Añadir datos de marcas
    marcas = Marca.objects.all()
    for row_num, marca in enumerate(marcas, 4):
        ws.cell(row=row_num, column=1, value=marca.id).alignment = alignment_center
        ws.cell(row=row_num, column=2, value=marca.nombre).alignment = alignment_center
        ws.cell(row=row_num, column=3, value='Activo' if marca.estado else 'Inactivo').alignment = alignment_center

    # Ajustar el ancho de las columnas
    column_widths = [5, 30, 10]  # Ajustar los anchos de columna según sea necesario
    for col_num, width in enumerate(column_widths, 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = width

    # Guardar el archivo en el buffer
    wb.save(buffer)
    buffer.seek(0)

    # Preparar la respuesta HTTP
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Reporte_marcas_samsamana.xlsx"'
    return response