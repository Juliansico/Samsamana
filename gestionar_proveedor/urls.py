
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    
    #proveedor
    path('proveedor/', views.gestionar_proveedor, name='gestionar_proveedor'),
    path('proveedor/añadir/', views.añadir_proveedor, name='añadir_proveedor'),
    path('proveedor/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedor/activar-inactivar/<int:proveedor_id>/', views.activar_inactivar_proveedor, name='activar_inactivar_proveedor'),
    path('filtrar_proveedores/', views.filtrar_proveedores, name='filtrar_proveedores'),
    path('reporte/proveedores/pdf/', views.reporte_proveedores_pdf, name='reporte_proveedores_pdf'),
    path('reporte/proveedores/excel/', views.reporte_proveedores_excel, name='reporte_proveedores_excel'),
]