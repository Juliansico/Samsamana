
from django.urls import path, include
from . import views
from .views import EliminarRespaldoView, CrearRespaldoView, RestaurarRespaldoView, descargar_respaldo, gestionar_respaldos

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('gestionar_respaldos/', gestionar_respaldos, name='gestionar_respaldos'),
    path('crear_respaldo/', CrearRespaldoView.as_view(), name='crear_respaldo'),
    path('restaurar_respaldo/', RestaurarRespaldoView.as_view(), name='restaurar_respaldo'),
    path('descargar_respaldo/<str:respaldo_id>/', descargar_respaldo, name='descargar_respaldo'),
    path('eliminar_respaldo/', EliminarRespaldoView.as_view(), name='eliminar_respaldo'),
   
    
    
    
]


