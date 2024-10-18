from django.db import models
from django.conf import settings
from gestionar_productos.models import Producto
from gestionar_usuarios.models import Usuario
from django.core.exceptions import ValidationError

class Venta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False)  # Este campo será obligatorio
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Total', default=0)

    def __str__(self):
        return f"Venta {self.id} - {self.usuario.username}"


    def calcular_total(self):
        # Sumar todos los subtotales de los detalles de la venta
        total = sum([detalle.subtotal for detalle in self.detalles.all()])
        self.valor_total = total
        self.save()


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio', default=0)

    def _str_(self):
        return f"Detalle de {self.venta} - {self.producto.nombre}"

    @property
    def subtotal(self):
        return self.cantidad * self.precio

    def save(self, *args, **kwargs):
        # Asigna el precio del producto automáticamente al guardar el detalle
        self.precio = self.producto.precio
        
        # Verificar que haya suficiente stock antes de guardar el detalle
        if self.cantidad > self.producto.stock:
            raise ValidationError(f"No hay suficiente stock de {self.producto.nombre}. Stock disponible: {self.producto.stock}")

        super().save(*args, **kwargs)

        # Reducir el stock del producto
        self.producto.stock -= self.cantidad
        self.producto.save()

        # Actualizar el total de la venta cada vez que se guarde un detalle
        self.venta.calcular_total()
