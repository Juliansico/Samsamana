# Generated by Django 4.0 on 2024-08-27 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionar_usuarios', '0002_alter_usuario_groups_alter_usuario_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_documento',
            field=models.CharField(choices=[('TI', 'Tarjeta de Identidad'), ('CC', 'Cédula de Ciudadanía')], max_length=2),
        ),
    ]
