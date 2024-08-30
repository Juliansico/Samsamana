# urls.py

from django.urls import path, include
from . import views

from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    #ventas
    path('ventas/', views.gestionar_ventas, name='gestionar_ventas'),
    path('ventas/añadir/', views.añadir_venta, name='añadir_venta'),
    path('ventas/consultar/', views.consultar_venta, name='consultar_venta'),
    path('ventas/activar-desactivar/<int:venta_id>/', views.activar_desactivar_venta, name='activar_desactivar_venta'),
    path('ventas/editar/<int:venta_id>/', views.editar_venta, name='editar_venta'),
    path('api/producto/<int:producto_id>/precio/', views.obtener_precio_producto, name='obtener_precio_producto'),
]