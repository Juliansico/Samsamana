from django.contrib import admin
from django.db import migrations

def create_groups_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Crear grupos
    productos_group, created = Group.objects.get_or_create(name='Productos')
    ventas_group, created = Group.objects.get_or_create(name='Ventas')
    presentacion_group, created = Group.objects.get_or_create(name='Presentacion')
    marca_group, created = Group.objects.get_or_create(name='Marca')
    categoria_group, created = Group.objects.get_or_create(name='Categoria')
    proveedor_group, created = Group.objects.get_or_create(name='Proveedor')
    compras_group, created = Group.objects.get_or_create(name='Compras')

    # Asignar permisos a los grupos (ajusta los permisos según tus modelos)
    productos_permissions = Permission.objects.filter(codename__in=['add_producto', 'change_producto', 'delete_producto', 'view_producto'])
    ventas_permissions = Permission.objects.filter(codename__in=['add_venta', 'change_venta', 'delete_venta', 'view_venta'])
    presentacion_permissions = Permission.objects.filter(codename__in=['add_presentacion', 'change_presentacion', 'delete_presentacion', 'view_presentacion'])
    marca_permissions = Permission.objects.filter(codename__in=['add_marca', 'change_marca', 'delete_marca', 'view_marca'])
    categoria_permissions = Permission.objects.filter(codename__in=['add_categoria', 'change_categoria', 'delete_categoria', 'view_categoria'])
    proveedor_permissions = Permission.objects.filter(codename__in=['add_proveedor', 'change_proveedor', 'delete_proveedor', 'view_proveedor'])
    compras_permissions = Permission.objects.filter(codename__in=['add_compra', 'change_compra', 'delete_compra', 'view_compra'])

    productos_group.permissions.set(productos_permissions)
    ventas_group.permissions.set(ventas_permissions)
    presentacion_group.permissions.set(presentacion_permissions)
    marca_group.permissions.set(marca_permissions)
    categoria_group.permissions.set(categoria_permissions)
    proveedor_group.permissions.set(proveedor_permissions)
    compras_group.permissions.set(compras_permissions)

class Migration(migrations.Migration):
    dependencies = [
        ('your_app_name', 'previous_migration_file'),
    ]

    operations = [
        migrations.RunPython(create_groups_and_permissions),
    ]
# Register your models here.
