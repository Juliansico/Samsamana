from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import  get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from django.contrib import messages
from .models import Venta, Producto, DetalleVenta
from .forms import VentaForm, DetalleVentaForm
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
from django.forms import inlineformset_factory

@login_required
@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')



@login_required
@never_cache
def crear_venta(request):
    DetalleVentaFormSet = inlineformset_factory(
        Venta, 
        DetalleVenta, 
        form=DetalleVentaForm, 
        extra=1,  # Puedes cambiar este número si no quieres formularios adicionales por defecto
        can_delete=True
    )
    
    if request.method == 'POST':
        form = VentaForm(request.POST)
        formset = DetalleVentaFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            venta = form.save()
            formset.instance = venta  # Asociar la venta a los detalles
            formset.save()

            # Imprimir el número de formularios en el formset
            print("Número de formularios en el formset:", formset.total_form_count())
            
            # Calcular y guardar el valor total
            valor_total = sum(detalle.subtotal for detalle in venta.detalles.all())
            venta.valor_total = valor_total
            venta.save()
            
            return redirect('gestionar_ventas')
        else:
            # Depuración de errores
            print(form.errors, formset.errors)  
    else:
        form = VentaForm()
        formset = DetalleVentaFormSet()
    
    return render(request, 'crear_venta.html', {'form': form, 'formset': formset})


@login_required
@never_cache
def gestionar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'gestionar_ventas.html', {'ventas': ventas})

@login_required
@never_cache
def detalle_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    return render(request, 'detalle_venta.html', {'venta': venta})

@login_required
@never_cache
def editar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    DetalleVentaFormSet = inlineformset_factory(Venta, DetalleVenta, form=DetalleVentaForm, extra=1)
    
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            venta = form.save(commit=False)
            formset = DetalleVentaFormSet(request.POST, instance=venta)
            if formset.is_valid():
                venta.save()
                formset.save()
                # Recalcular y guardar el valor total
                valor_total = sum(detalle.subtotal for detalle in venta.detalles.all())
                venta.valor_total = valor_total
                venta.save()
                return redirect('gestionar_ventas')
    else:
        form = VentaForm(instance=venta)
        formset = DetalleVentaFormSet(instance=venta)
    
    return render(request, 'editar_venta.html', {'form': form, 'formset': formset})

@login_required
@never_cache
def eliminar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, 'La venta ha sido eliminada exitosamente.')
        return redirect('gestionar_ventas')
    return render(request, 'eliminar_venta.html', {'venta': venta})





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
    p.drawCentredString(width / 2, y_position, "SAMSAMANA")
    y_position -= 30
    p.setFont("Helvetica", 18)
    p.drawCentredString(width / 2, y_position, "Reporte de Ventas")
    y_position -= 50

    # Crear tabla con datos de ventas
    column_widths = [30, 100, 80, 100, 80, 90]
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

    # Calcular el ancho total de la tabla
    table_width = sum(column_widths)
    
    # Calcular la posición x para centrar la tabla
    table_x = (width - table_width) / 2
    
    # Ajustar la posición y de la tabla
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

    # Añadir logo (más pequeño) en la celda A1
    logo_path = os.path.join(settings.STATIC_ROOT, 'img', 'Samsamanalogo1PNG.png')
    if os.path.exists(logo_path):
        img = Image(logo_path)
        img.width = 80  # Ajustar tamaño según necesidad
        img.height = 40
        ws.add_image(img, 'A1')

    # Añadir título
    ws.merge_cells('B1:G1')
    title_cell = ws['B1']
    title_cell.value = "TABLA VENTAS - BALNEARIO SAMSAMANA"
    title_cell.font = Font(bold=True, size=16)
    title_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Añadir encabezados
    headers = ["ID", "Producto", "Cantidad", "Fecha", "Total", "Estado"]
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=2, column=col_num, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = alignment_center

    # Añadir datos de ventas
    ventas = Venta.objects.all()
    for row_num, venta in enumerate(ventas, 3):
        ws.cell(row=row_num, column=1, value=venta.id).alignment = alignment_center
        ws.cell(row=row_num, column=2, value=str(venta.producto)).alignment = alignment_center
        ws.cell(row=row_num, column=3, value=venta.cantidad_Venta).alignment = alignment_center
        ws.cell(row=row_num, column=4, value=venta.fecha.strftime('%Y-%m-%d %H:%M:%S')).alignment = alignment_center
        ws.cell(row=row_num, column=5, value=venta.total_Venta).alignment = alignment_center
        ws.cell(row=row_num, column=6, value='Activo' if venta.estado else 'Inactivo').alignment = alignment_center

    # Ajustar el ancho de las columnas
    column_widths = [10, 30, 15, 20, 20, 15]  # Ajusta los anchos según sea necesario
    for col_num, width in enumerate(column_widths, 1):
        column_letter = get_column_letter(col_num)
        ws.column_dimensions[column_letter].width = width

    # Guardar el archivo en el buffer
    wb.save(buffer)
    buffer.seek(0)

    # Preparar la respuesta HTTP
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Reporte_ventas.xlsx"'
    return response
