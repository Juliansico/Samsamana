from django.shortcuts import render, redirect, get_object_or_404
from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.utils import ImageReader
import os
from openpyxl.drawing.image import Image
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import  Categoria
from .forms import  CategoriaForm
from openpyxl.utils import get_column_letter
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
# Create your views here.

@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')
@never_cache
@login_required
def gestionar_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestionar_categoria.html', {'categorias': categorias})


@never_cache
@login_required
def añadir_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría añadida con éxito.')
            return redirect('gestionar_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'añadir_categoria.html', {'form': form})


@never_cache
@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada con éxito.')
            return redirect('gestionar_categoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form, 'categoria': categoria})


@never_cache
@login_required
def activar_inactivar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.estado = not categoria.estado
    categoria.save()
    estado = "activada" if categoria.estado else "inactivada"
    messages.success(request, f'Categoría {estado} con éxito.')
    return redirect('gestionar_categoria')

@never_cache
@login_required
def filtrar_categorias(request):
    estado_filtro = request.GET.get('estado', None)
    buscar = request.GET.get('buscar', '')

    categorias = Categoria.objects.all()

    if estado_filtro == 'activado':
        categorias = categorias.filter(estado=True)
    elif estado_filtro == 'inactivado':
        categorias = categorias.filter(estado=False)

    if buscar:
        categorias = categorias.filter(nombre__icontains=buscar)

    context = {
        'categorias': categorias,
    }

    return render(request, 'gestionar_categoria.html', context)


def reporte_categorias_pdf(request):
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
            p.setFillAlpha(0.5)
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
    p.drawString(margin, y_position, "Reporte de Categorías")
    y_position -= 50

    # Crear tabla con datos de categorías
    headers = ["ID", "Nombre", "Estado"]
    data = [headers]

    categorias = Categoria.objects.all()
    for categoria in categorias:
        data.append([
            str(categoria.id),
            categoria.nombre,
            'Activo' if categoria.estado else 'Inactivo'
        ])

    column_widths = [50, 200, 100]
    table = Table(data, colWidths=column_widths)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#25b6e6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f2f2f2')),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
    ])
    table.setStyle(style)

    # Ajustar la posición de la tabla
    table.wrapOn(p, width, height)
    table.drawOn(p, margin, y_position - len(data) * row_height)

    p.showPage()
    p.save()
    buffer.seek(0)

    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Reporte_categorias.pdf"'
    return response


def reporte_categorias_excel(request):
    # Crear un archivo Excel en memoria
    buffer = BytesIO()
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte de Categorías"

    # Definir estilos
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="25b6e6", end_color="25b6e6", fill_type="solid")
    alignment_center = Alignment(horizontal="center", vertical="center")

    # Añadir encabezados
    headers = ["ID", "Nombre", "Estado"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = alignment_center

    # Añadir datos de categorías
    categorias = Categoria.objects.all()
    for row_num, categoria in enumerate(categorias, 2):
        ws.cell(row=row_num, column=1, value=categoria.id)
        ws.cell(row=row_num, column=2, value=categoria.nombre)
        ws.cell(row=row_num, column=3, value='Activo' if categoria.estado else 'Inactivo')

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
    response['Content-Disposition'] = 'attachment; filename="Reporte_categorias.xlsx"'
    return response