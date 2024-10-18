from django.db import models
from gestionar_usuarios.models import Usuario  # O el modelo que uses para los usuarios
from gestionar_proveedor.models import Proveedor  # Proveedor que asocias con las compras
from gestionar_productos.models import Producto
from django.utils import timezone

class Compra(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    cantidad_productos = models.IntegerField(default=0)
    total_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    estado = models.BooleanField(default=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def str(self):
        return f"Compra {self.id} - {self.usuario.username}"

    def calcular_total(self):
        
        total_compra = sum([detalle.subtotal for detalle in self.detalles.all()])
        self.total_compra = total_compra
        self.save()

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio', default=0)

    def str(self):
        return f"Detalle de {self.compra} - {self.producto.nombre}"

    @property
    def subtotal(self):
        return self.precio


    def save(self, *args, **kwargs):
        # Asigna el precio del producto automáticamente al guardar el detalle
        self.precio = self.producto.precio
        super().save(*args, **kwargs)

        self.compra.calcular_total()

    @property
    def proveedor(self):
        # Obtiene el proveedor directamente desde el producto asociado
        return self.producto.proveedor
    
    def save(self, *args, **kwargs):
        # Al guardar un detalle de compra, se aumenta el stock del producto
        if self.pk is None:  # Solo sumar el stock si es un nuevo detalle de compra
            self.producto.stock += self.cantidad
            self.producto.save()
        super().save(*args, **kwargs)