# Generated by Django 5.0.7 on 2024-08-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionar_ventas', '0004_rename_fecha_apertura_venta_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='total_Venta_Realizada',
        ),
        migrations.AddField(
            model_name='venta',
            name='total_Venta',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
