# Generated by Django 5.0.7 on 2024-08-30 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionar_ventas', '0003_remove_venta_fecha_cierre_remove_venta_saldo_actual_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='fecha_Apertura',
            new_name='fecha',
        ),
    ]
