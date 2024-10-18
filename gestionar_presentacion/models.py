from django.db import models

class Presentacion(models.Model):
    nombre = models.CharField(max_length=255, unique=True)  # Haciendo el campo nombre único
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
