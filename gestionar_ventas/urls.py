from django.urls import path, include
from . import views

from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/producto/<int:producto_id>/precio/', views.obtener_precio_producto, name='obtener_precio_producto'),
    path('reporte/ventas/pdf/', views.reporte_ventas_pdf, name='reporte_ventas_pdf'),
    path('reporte/ventas/excel/', views.reporte_ventas_excel, name='reporte_ventas_excel'),
    path('ventas/', views.gestionar_ventas, name='gestionar_ventas'),
    path('ventas/crear/', views.crear_venta, name='crear_venta'),
    path('ventas/<int:id>/', views.detalle_venta, name='detalle_venta'),
    path('ventas/<int:id>/editar/', views.editar_venta, name='editar_venta'),
    path('ventas/<int:id>/eliminar/', views.eliminar_venta, name='eliminar_venta'),
]
