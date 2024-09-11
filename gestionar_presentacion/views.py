from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Presentacion
from .forms import PresentacionForm
from django.views.decorators.cache import never_cache
from io import BytesIO
from django.http import HttpResponse
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image
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

@never_cache
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


@never_cache
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

def reporte_presentaciones_pdf(request):
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
    p.drawString(margin, y_position, "Reporte de Presentaciones")
    y_position -= 50

    # Crear tabla con datos de presentaciones
    column_widths = [50, 150, 60]
    headers = ["ID", "Nombre", "Estado"]
    data = [headers]

    presentaciones = Presentacion.objects.all()
    for presentacion in presentaciones:
        data.append([
            str(presentacion.id),
            presentacion.nombre,
            'Activo' if presentacion.estado else 'Inactivo'
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
    response['Content-Disposition'] = 'attachment; filename="Reporte_presentaciones.pdf"'
    return response


def reporte_presentaciones_excel(request):
    # Crear buffer para el archivo Excel
    buffer = BytesIO()

    # Crear el libro y la hoja de cálculo
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte de Presentaciones"

    # Definir estilos para encabezados
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="25b6e6", end_color="25b6e6", fill_type="solid")
    alignment_center = Alignment(horizontal="center", vertical="center")

    # Añadir logo
    logo_path = os.path.join(settings.STATIC_ROOT, 'img', 'Samsamanalogo1PNG.png')
    if os.path.exists(logo_path):
        img = Image(logo_path)
        img.width = 150  # Ajustar tamaño según sea necesario
        img.height = 75  # Ajustar tamaño según sea necesario
        ws.add_image(img, 'A1')

    # Añadir título
    ws.merge_cells('B1:D1')  # Ajusta el rango según el número de columnas
    title_cell = ws['B1']
    title_cell.value = "Reporte de Presentaciones - Balneario Samsamana"
    title_cell.font = Font(bold=True, size=16)
    title_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Añadir encabezados
    headers = ["ID", "Nombre", "Estado"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=2, column=col_num, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = alignment_center

    # Añadir datos de presentaciones
    presentaciones = Presentacion.objects.all()
    for row_num, presentacion in enumerate(presentaciones, 3):  # Fila inicial para datos es 3
        ws.cell(row=row_num, column=1, value=presentacion.id).alignment = alignment_center
        ws.cell(row=row_num, column=2, value=presentacion.nombre).alignment = alignment_center
        ws.cell(row=row_num, column=3, value='Activo' if presentacion.estado else 'Inactivo').alignment = alignment_center

    # Ajustar el ancho de las columnas
    column_widths = [10, 30, 20]  # Ajusta los anchos según el contenido
    for col_num, width in enumerate(column_widths, 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = width

    # Guardar el archivo en el buffer
    wb.save(buffer)
    buffer.seek(0)

    # Preparar la respuesta HTTP
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Reporte_presentaciones.xlsx"'
    
    return response











