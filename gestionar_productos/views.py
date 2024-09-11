from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
from gestionar_categoria.models import Categoria
from gestionar_marca.models import Marca
from gestionar_presentacion.models import Presentacion
import logging
import os
from reportlab.lib.utils import ImageReader
from django.views.decorators.cache import never_cache
from django.conf import settings
from io import BytesIO
from django.http import HttpResponse
from django.contrib.staticfiles import finders
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.colors import Color
from .models import Producto
from openpyxl.drawing.image import Image
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from io import BytesIO
# Create your views here.

@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')
@never_cache
@login_required
def gestionar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestionar_productos.html', {'productos': productos})

@never_cache
@login_required
def añadir_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto añadido con éxito.')
            return redirect('gestionar_productos')
    else:
        form = ProductoForm()
    return render(request, 'añadir_producto.html', {'form': form})


@never_cache
@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado con éxito.')
            return redirect('gestionar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

@never_cache
@login_required
def filtrar_productos(request):
    estado_filtro = request.GET.get('estado', None)
    buscar = request.GET.get('buscar', '')
    precio_min = request.GET.get('precio_min', None)
    precio_max = request.GET.get('precio_max', None)
    categoria_id = request.GET.get('categoria', '')
    marca_id = request.GET.get('marca', '')
    presentacion_id = request.GET.get('presentacion', '')

    productos = Producto.objects.all()

    if estado_filtro == 'activado':
        productos = productos.filter(estado=True)
    elif estado_filtro == 'inactivado':
        productos = productos.filter(estado=False)

    if buscar:
        productos = productos.filter(nombre__icontains=buscar)
    if precio_min:
        productos = productos.filter(precio__gte=precio_min)
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    if marca_id:
        productos = productos.filter(marca_id=marca_id)
    if presentacion_id:
        productos = productos.filter(presentacion_id=presentacion_id)
    

    context = {
        'productos': productos,
        'categorias': Categoria.objects.all(),
        'marcas': Marca.objects.all(),
        'presentaciones': Presentacion.objects.all(),
    }

    return render(request, 'gestionar_productos.html', context)
@never_cache
@login_required
def activar_inactivar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.estado = not producto.estado
    producto.save()
    estado = "activado" if producto.estado else "inactivado"
    messages.success(request, f'Producto {estado} con éxito.')
    return redirect('gestionar_productos')


def reporte_productos_pdf(request):
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
    p.drawString(margin, y_position, "Reporte de Productos")
    y_position -= 50


    column_widths = [30, 150, 80, 60, 60, 80, 60, 60]
    headers = ["ID", "Nombre", "Marca", "Presentación", "Categoría", "Precio", "Unidad de medida", "Estado"]
    data = [headers]

    productos = Producto.objects.all()
    for producto in productos:
        data.append([
            str(producto.id),
            producto.nombre,
            producto.marca.nombre,
            producto.presentacion.nombre,
            producto.categoria.nombre,
            str(producto.precio),
            producto.unidad_de_medida,
            'Activo' if producto.estado else 'Inactivo'
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
    response['Content-Disposition'] = 'attachment; filename="Reporte_productos.pdf"'
    return response

def reporte_productos_excel(request):
    buffer = BytesIO()
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte de Productos"

    # Definir estilos
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="25b6e6", end_color="25b6e6", fill_type="solid")
    alignment_center = Alignment(horizontal="center", vertical="center")
    
    # Añadir logo (más pequeño)
    logo_path = os.path.join(settings.STATIC_ROOT, 'img', 'Samsamanalogo1PNG.png')
    if os.path.exists(logo_path):
        img = Image(logo_path)
        img.width = 80  # Hacer el logo más pequeño (ajustar según necesidad)
        img.height = 40
        ws.add_image(img, 'A1')

    # Añadir título
    ws.merge_cells('B1:H1')
    title_cell = ws['B1']
    title_cell.value = "TABLA PRODUCTOS - BALNEARIO SAMSAMANA"
    title_cell.font = Font(bold=True, size=16)
    title_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Añadir encabezados
    headers = ["ID", "Nombre", "Marca", "Presentación", "Categoría", "Precio", "Unidad de medida", "Estado"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col_num, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = alignment_center

    # Añadir datos de productos
    productos = Producto.objects.all()
    for row_num, producto in enumerate(productos, 4):
        ws.cell(row=row_num, column=1, value=producto.id).alignment = alignment_center
        ws.cell(row=row_num, column=2, value=producto.nombre).alignment = alignment_center
        ws.cell(row=row_num, column=3, value=producto.marca.nombre).alignment = alignment_center
        ws.cell(row=row_num, column=4, value=producto.presentacion.nombre).alignment = alignment_center
        ws.cell(row=row_num, column=5, value=producto.categoria.nombre).alignment = alignment_center
        ws.cell(row=row_num, column=6, value=producto.precio).alignment = alignment_center
        ws.cell(row=row_num, column=7, value=producto.unidad_de_medida).alignment = alignment_center
        ws.cell(row=row_num, column=8, value='Activo' if producto.estado else 'Inactivo').alignment = alignment_center

    # Ajustar el ancho de las columnas para que se vean centradas
    column_widths = [5, 20, 20, 20, 20, 15, 30, 10]  # Ajusta los anchos según sea necesario
    for col_num, width in enumerate(column_widths, 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = width

    # Guardar el archivo en el buffer
    wb.save(buffer)
    buffer.seek(0)

    # Preparar la respuesta HTTP
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Reporte_productos_samsamana.xlsx"'
    return response
