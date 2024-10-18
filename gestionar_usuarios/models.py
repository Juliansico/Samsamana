from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_DOCUMENTO_CHOICES = [
        ('TI', 'Tarjeta de Identidad'),
        ('CC', 'Cédula de Ciudadanía'),
    ]
    
    reset_token = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=150)
    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO_CHOICES)
    documento = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=254, unique=True)
    estado = models.BooleanField(default=True)
    estado = models.BooleanField(default=True)

    def is_active_user(self):
        return self.is_active and self.estado

    @property
    def is_active(self):
        return self.estado

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuario',
    )

    def __str__(self):
        return self.username