from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views import View
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
import os
import subprocess
from datetime import datetime
from .models import Respaldo



def get_breadcrumbs(request):
    path = request.path.split('/')[1:]
    breadcrumbs = [{'title': 'Inicio', 'url': '/dashboard/'}]  # El inicio te lleva al dashboard
    url = ''
    for item in path:
        url += f'/{item}'
        breadcrumbs.append({'title': item.capitalize(), 'url': url})
    return breadcrumbs

User = get_user_model()


@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')


# Vista para listar los respaldos
@never_cache
def gestionar_respaldos(request):
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    print(f"Ruta del directorio de respaldos: {backup_dir}")

    # Crear el directorio si no existe
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backups = []
    try:
        for filename in os.listdir(backup_dir):
            if filename.endswith('.sql'):
                file_path = os.path.join(backup_dir, filename)
                created_at = datetime.fromtimestamp(os.path.getctime(file_path))
                size = os.path.getsize(file_path)
                backups.append({
                    'id': filename,
                    'filename': filename,
                    'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'size': f"{size / 1024 / 1024:.2f} MB"
                })
    except FileNotFoundError:
        messages.error(request, "No se pudo encontrar el directorio de respaldos.")

    backups.sort(key=lambda x: x['created_at'], reverse=True)

    # Paginación
    paginator = Paginator(backups, 10)  # 10 respaldos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    breadcrumbs = get_breadcrumbs(request)
    return render(request, 'gestionar_respaldos.html', {'page_obj': page_obj, 'breadcrumbs': breadcrumbs})

# Vista para crear un respaldo de la base de datos
@method_decorator(never_cache, name='post')
class CrearRespaldoView(View):
    def post(self, request, *args, **kwargs):
        try:
            # Obtener la configuración de la base de datos
            db_settings = settings.DATABASES['default']
            db_name = db_settings['NAME']
            db_user = db_settings['USER']
            db_password = db_settings['PASSWORD']
            db_host = db_settings['HOST']
            db_port = db_settings['PORT']

            # Crear el nombre del archivo de respaldo
            filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
            backup_dir = os.path.join(settings.BASE_DIR, 'backups')
            backup_path = os.path.join(backup_dir, filename)

            # Asegurarse de que el directorio de respaldos existe
            os.makedirs(backup_dir, exist_ok=True)

            # Usa la ruta completa a mysqldump.exe
            mysqldump_path = r"C:\Program Files\MySQL\MySQL Server 9.0\bin\mysqldump.exe"

            # Comando para crear el respaldo
            command = (
                f"\"{mysqldump_path}\" -h {db_host} -P {db_port} -u {db_user} -p{db_password} "
                f"{db_name} > \"{backup_path}\""
            )

            # Ejecutar el comando y capturar la salida
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                messages.error(request, f"Error al crear el respaldo: {result.stderr}")
            else:
                messages.success(request, f"Respaldo creado exitosamente: {filename}")
        except Exception as e:
            messages.error(request, f"Error al crear el respaldo: {str(e)}")

        return redirect('gestionar_respaldos')

@method_decorator(never_cache, name='post')
class RestaurarRespaldoView(View):
    def post(self, request, *args, **kwargs):
        # Obtener el nombre del archivo desde el campo oculto
        backup_id = request.POST.get('respaldo_id')

        if backup_id:
            try:
                # Obtener la configuración de la base de datos
                db_settings = settings.DATABASES['default']
                db_name = db_settings['NAME']
                db_user = db_settings['USER']
                db_password = db_settings['PASSWORD']
                db_host = db_settings['HOST']
                db_port = db_settings['PORT']

                # Construir la ruta del archivo de respaldo
                backup_dir = os.path.join(settings.BASE_DIR, 'backups')
                backup_path = os.path.join(backup_dir, backup_id)

                # Verificar que el archivo de respaldo existe
                if not os.path.exists(backup_path):
                    print(f"El archivo de respaldo no existe en: {backup_path}")  # Línea añadida para depuración
                    messages.error(request, "El archivo de respaldo especificado no existe.")
                    return redirect('gestionar_respaldos')

                # Escapar la ruta del archivo para evitar problemas con espacios
                backup_path_escaped = f"\"{backup_path}\""

                # Comando para restaurar la base de datos
                mysql_path = r'"C:\Program Files\MySQL\MySQL Server 9.0\bin\mysql.exe"'  # Ruta completa al ejecutable de mysql
                command = (
                    f"{mysql_path} -h {db_host} -P {db_port} -u {db_user} -p{db_password} "
    f"{db_name} < {backup_path_escaped}"
)

                # Ejecutar el comando y capturar la salida
                result = subprocess.run(command, shell=True, capture_output=True, text=True)

                if result.returncode != 0:
                    messages.error(request, f"Error al restaurar la base de datos: {result.stderr}")
                    print(f"Error: {result.stderr}")  # Imprimir error en consola para depuración
                else:
                    messages.success(request, f"Base de datos restaurada desde {backup_id}")

            except subprocess.CalledProcessError as e:
                messages.error(request, f"Error al ejecutar el comando de restauración: {e}")
            except Exception as e:
                messages.error(request, f"Error inesperado al restaurar la base de datos: {str(e)}")
        else:
            messages.error(request, "No se especificó un archivo para restaurar")

        return redirect('gestionar_respaldos')

# Vista para descargar un respaldo
@never_cache
def descargar_respaldo(request, respaldo_id):
    file_path = os.path.join(settings.BASE_DIR, 'backups', respaldo_id)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            breadcrumbs = get_breadcrumbs(request)
            response['breadcrumbs'] = breadcrumbs  # Añadir breadcrumbs a la respuesta, si es necesario
            return response
    raise Http404

# Vista para eliminar un respaldo
@method_decorator(never_cache, name='post')
class EliminarRespaldoView(View):
    def post(self, request, *args, **kwargs):
        respaldo_id = request.POST.get('respaldo_id')
        if respaldo_id:
            file_path = os.path.join(settings.BASE_DIR, 'backups', respaldo_id)
            
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    messages.success(request, f"Respaldo {respaldo_id} eliminado exitosamente")
                except Exception as e:
                    messages.error(request, f"Error al eliminar el archivo: {str(e)}")
            else:
                messages.error(request, f"El archivo {respaldo_id} no existe")
        else:
            messages.error(request, "No se especificó un archivo para eliminar")

        return redirect('gestionar_respaldos')


