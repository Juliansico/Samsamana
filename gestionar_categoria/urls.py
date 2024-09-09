from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),   
    path('categoria/', views.gestionar_categoria, name='gestionar_categoria'),
    path('categoria/añadir/', views.añadir_categoria, name='añadir_categoria'),
    path('categoria/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/activar-inactivar/<int:categoria_id>/', views.activar_inactivar_categoria, name='activar_inactivar_categoria'),
    path('categorias/', views.filtrar_categorias, name='filtrar_categorias'),
    path('reporte-categorias/pdf/', views.reporte_categorias_pdf, name='reporte_categorias_pdf'),
    path('reporte-categorias/excel/', views.reporte_categorias_excel, name='reporte_categorias_excel'),
    
]