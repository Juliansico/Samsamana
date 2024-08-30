from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('marca/', views.gestionar_marca, name='gestionar_marca'),
    path('marca/añadir/', views.añadir_marca, name='añadir_marca'),
    path('marca/editar/<int:marca_id>/', views.editar_marca, name='editar_marca'),
    path('marca/activar-inactivar/<int:marca_id>/', views.activar_inactivar_marca, name='activar_inactivar_marca'),
    path('marcas/', views.filtrar_marcas, name='filtrar_marcas'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)