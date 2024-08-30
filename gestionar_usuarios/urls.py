
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    #usuario
    path('usuarios/', views.gestionar_usuarios, name='gestionar_usuarios'),
    path('usuarios/añadir/', views.añadir_usuario, name='añadir_usuario'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/activar-inactivar/<int:usuario_id>/', views.activar_inactivar_usuario, name='activar_inactivar_usuario'),
    path('filtrar_usuarios', views.filtrar_usuarios, name='filtrar_usuarios'),
    
]