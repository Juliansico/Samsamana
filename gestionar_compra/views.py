
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import  Compra
from .forms import  CompraForm
from openpyxl.drawing.image import Image
from reportlab.lib.utils import ImageReader
from django.views.decorators.cache import never_cache
from io import BytesIO
from django.http import HttpResponse
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import os
# Create your views here.
@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')
@never_cache
@login_required
def gestionar_compra(request):
    compras = Compra.objects.all()
    return render(request, 'gestionar_compra.html', {'compras': compras})


@never_cache
@login_required
def añadir_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compra añadida con éxito.')
            return redirect('gestionar_compra')
    else:
        form = CompraForm()
    return render(request, 'añadir_compra.html', {'form': form})

@never_cache

@login_required
def editar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compra actualizada con éxito.')
            return redirect('gestionar_compra')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'editar_compra.html', {'form': form, 'compra': compra})



@login_required
def activar_inactivar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    compra.estado = not compra.estado
    compra.save()
    messages.success(request, f'Compra {compra.estado} con éxito.')
    return redirect('gestionar_compra')


@never_cache
@login_required
def consultar_compra(request):
    if request.method == 'POST':
        id_compra = request.POST.get('id_compra')
        fecha_compra = request.POST.get('fecha_compra')
        proveedor = request.POST.get('proveedor')
        estado = request.POST.get('estado')
        
        compras = Compra.objects.all()
        if id_compra:
            compras = compras.filter(id=id_compra)
        if fecha_compra:
            compras = compras.filter(fechaCompra__date=fecha_compra)
        if proveedor:
            compras = compras.filter(proveedorId__nombre__icontains=proveedor)
        if estado:
            compras = compras.filter(estadoCompra=estado)
        
        return render(request, 'consultar_compra.html', {'compras': compras})
    return render(request, 'consultar_compra.html')

def reporte_compras_pdf(request):
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
    p.drawString(margin, y_position, "Reporte de Compras")
    y_position -= 50

    # Crear tabla con datos de compras
    column_widths = [30, 80, 80, 80, 80, 60]
    headers = ["ID", "Fecha Compra", "Total Compra", "Cantidad Producto", "Proveedor", "Estado"]
    data = [headers]

    compras = Compra.objects.all()
    for compra in compras:
        data.append([
            str(compra.id),
            compra.fecha_Compra.strftime('%Y-%m-%d %H:%M:%S'),
            str(compra.total_Compra),
            str(compra.cantidad_Producto),
            compra.proveedor_Id.nombre,  # Asegúrate de que `nombre` es un atributo de `Proveedor`
            'Activo' if compra.estado else 'Inactivo'
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
    response['Content-Disposition'] = 'attachment; filename="Reporte_compras.pdf"'
    return response



def reporte_compras_excel(request):
    # Crear un archivo Excel en memoria
    buffer = BytesIO()
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte de Compras"

    # Definir estilos
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="25b6e6", end_color="25b6e6", fill_type="solid")
    alignment_center = Alignment(horizontal="center", vertical="center")

    # Añadir encabezados
    headers = ["ID", "Fecha Compra", "Total Compra", "Cantidad Producto", "Proveedor", "Estado"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = alignment_center

    # Añadir datos de compras
    compras = Compra.objects.all()
    for row_num, compra in enumerate(compras, 2):
        ws.cell(row=row_num, column=1, value=compra.id)
        ws.cell(row=row_num, column=2, value=compra.fecha_Compra.strftime('%Y-%m-%d %H:%M:%S'))
        ws.cell(row=row_num, column=3, value=compra.total_Compra)
        ws.cell(row=row_num, column=4, value=compra.cantidad_Producto)
        ws.cell(row=row_num, column=5, value=compra.proveedor_Id.nombre)  # Asegúrate de que `nombre` es un atributo de `Proveedor`
        ws.cell(row=row_num, column=6, value='Activo' if compra.estado else 'Inactivo')

    # Ajustar el ancho de las columnas
    for col_num in range(1, len(headers) + 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = 20

    # Añadir imagen de marca de agua
    watermark_path = os.path.join(settings.STATIC_ROOT, 'img', 'Samsamanalogo1PNG.png')
    if os.path.exists(watermark_path):
        try:
            img = Image(watermark_path)
            img.anchor = 'A1'  # Anclar la imagen en la celda A1
            img.width = 400  # Ajusta el tamaño de la imagen según sea necesario
            img.height = 300
            ws.add_image(img)
        except Exception as e:
            print("Error al agregar la marca de agua en Excel:", e)

    # Guardar el archivo en el buffer
    wb.save(buffer)
    buffer.seek(0)

    # Preparar la respuesta HTTP
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Reporte_compras.xlsx"'
    return response
