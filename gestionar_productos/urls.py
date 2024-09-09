from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('reporte_excel/', views.reporte_productos_excel, name='reporte_productos_excel'),
    path('productos/reportes/pdf/', views.reporte_productos_pdf, name='reporte_productos_pdf'),
    path('productos/', views.gestionar_productos, name='gestionar_productos'),
    path('productos/añadir/', views.añadir_producto, name='añadir_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/activar-inactivar/<int:producto_id>/', views.activar_inactivar_producto, name='activar_inactivar_producto'),
    path('filtrar_productos/', views.filtrar_productos, name='filtrar_productos'),
    
]