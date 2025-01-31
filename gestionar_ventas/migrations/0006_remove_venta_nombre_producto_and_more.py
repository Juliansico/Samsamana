# Generated by Django 5.0.7 on 2024-08-30 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionar_productos', '0001_initial'),
        ('gestionar_ventas', '0005_remove_venta_total_venta_realizada_venta_total_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='nombre_Producto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='precio_Producto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='productos',
        ),
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionar_productos.producto'),
            preserve_default=False,
        ),
    ]
