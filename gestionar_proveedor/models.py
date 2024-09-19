from django.db import models


# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre