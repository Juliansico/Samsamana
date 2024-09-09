from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import  get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from django.contrib import messages
from .models import Venta, Producto
from .forms import VentaForm
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
from openpyxl.drawing.image import Image
@never_cache
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
@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')
@never_cache
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

@never_cache
@login_required
def consultar_venta(request):
    if request.method == 'POST':
        id_venta = request.POST.get('id_venta')
        ventas = Venta.objects.filter(id=id_venta)
        return render(request, 'consultar_venta.html', {'ventas': ventas})
    return render(request, 'consultar_venta.html')

@never_cache
@login_required
def añadir_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.id_Usuario = request.user
            venta.save()
            messages.success(request, 'Venta añadida con éxito.')
            return redirect('gestionar_ventas')
    else:
        form = VentaForm()
    return render(request, 'añadir_venta.html', {'form': form})
@never_cache
@login_required
def activar_desactivar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id, id_Usuario=request.user)
    venta.estado = not venta.estado
    estado = "activada" if venta.estado else "inactivada" 
    messages.success(request, f'Venta {estado} con éxito.')
    venta.save()
    return redirect('gestionar_ventas')


from django.http import JsonResponse
@never_cache
def obtener_precio_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return JsonResponse({'precio': producto.precio})

def reporte_ventas_pdf(request):
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
    p.drawString(margin, y_position, "Reporte de Ventas")
    y_position -= 50

    # Crear tabla con datos de ventas
    column_widths = [50, 150, 100, 150, 100, 100]
    headers = ["ID", "Producto", "Cantidad", "Fecha", "Total", "Estado"]
    data = [headers]

    ventas = Venta.objects.all()
    for venta in ventas:
        data.append([
            str(venta.id),
            str(venta.producto),
            venta.cantidad_Venta,
            venta.fecha.strftime('%Y-%m-%d %H:%M:%S'),
            venta.total_Venta,
            'Activo' if venta.estado else 'Inactivo'
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
    response['Content-Disposition'] = 'attachment; filename="Reporte_ventas.pdf"'
    return response

def reporte_ventas_excel(request):
    # Crear un archivo Excel en memoria
    buffer = BytesIO()
    wb = Workbook()
    ws = wb.active
    ws.title = "Reporte de Ventas"

    # Definir estilos
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="25b6e6", end_color="25b6e6", fill_type="solid")
    alignment_center = Alignment(horizontal="center", vertical="center")

    # Añadir encabezados
    headers = ["ID", "Producto", "Cantidad", "Fecha", "Total", "Estado"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = alignment_center

    # Añadir datos de ventas
    ventas = Venta.objects.all()
    for row_num, venta in enumerate(ventas, 2):
        ws.cell(row=row_num, column=1, value=venta.id)
        ws.cell(row=row_num, column=2, value=str(venta.producto))
        ws.cell(row=row_num, column=3, value=venta.cantidad_Venta)
        ws.cell(row=row_num, column=4, value=venta.fecha.strftime('%Y-%m-%d %H:%M:%S'))
        ws.cell(row=row_num, column=5, value=venta.total_Venta)
        ws.cell(row=row_num, column=6, value='Activo' if venta.estado else 'Inactivo')

    # Ajustar el ancho de las columnas
    for col_num in range(1, len(headers) + 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = 20

    # Añadir la imagen de marca de agua centrada
    watermark_path = os.path.join(settings.STATIC_ROOT, 'img', 'Samsamanalogo1PNG.png')
    if os.path.exists(watermark_path):
        try:
            img = Image(watermark_path)
            
            # Ajustar el tamaño de la imagen
            img.width = 500  # Ajusta según sea necesario
            img.height = 300  # Ajusta según sea necesario

            # Calcular el centro de la hoja
            max_row = ws.max_row + 5  # Añadir espacio adicional si es necesario
            max_col = ws.max_column
            center_col = (max_col + 1) // 2  # Columna central
            center_row = (max_row + 1) // 2  # Fila central
            center_cell = f"{get_column_letter(center_col)}{center_row}"

            # Colocar la imagen en la celda central
            ws.add_image(img, center_cell)

        except Exception as e:
            print("Error al agregar la marca de agua:", e)

    # Guardar el archivo en el buffer
    wb.save(buffer)
    buffer.seek(0)

    # Preparar la respuesta HTTP
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Reporte_ventas.xlsx"'
    return response
