from django.db import models
from django.conf import settings
from gestionar_productos.models import Producto


class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_Venta = models.FloatField()
    total_Venta = models.FloatField() 
    estado = models.BooleanField(default=True)
    fecha = models.DateTimeField()
    id_Usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.total_Venta = self.producto.precio * self.cantidad_Venta
        super().save(*args, **kwargs)

class Ventas_has_producto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
# Create your models here.
