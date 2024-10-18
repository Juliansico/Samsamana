from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('compra/', views.gestionar_compras, name='gestionar_compras'),
    path('compra/añadir/', views.crear_compra, name='crear_compra'),
    path('api/producto/<int:producto_id>/precio/', views.obtener_precio_y_proveedor, name='obtener_precio_y_proveedor'),
    path('compras/<int:id>/eliminar/', views.eliminar_compra, name='eliminar_compra'),
    path('compras/<int:id>/', views.detalle_compra, name='detalle_compra'),
    path('reporte-compras/pdf/', views.reporte_compras_pdf, name='reporte_compras_pdf'),
    path('reporte-compras/excel/', views.reporte_compras_excel, name='reporte_compras_excel'),
    path('detalle_compra/<int:id>/exportar/pdf/', views.exportar_detalle_compra_pdf, name='exportar_detalle_compra_pdf'),
    path('detalle_compra/<int:id>/exportar/excel/', views.exportar_detalle_compra_excel, name='exportar_detalle_compra_excel'),
    ]
