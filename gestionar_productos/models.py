from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Producto(models.Model):
    UNIDADES_MEDIDA = [
        ('KG', 'Kilogramo'),
        ('HG', 'Hectogramo'),
        ('G', 'Gramo'),
        ('DAG', 'Decagramo'),
        ('DG', 'Decigramo'),
        ('CG', 'Centigramo'),
        ('MG', 'Miligramo'),
        ('KL', 'Kilolitro'),
        ('HL', 'Hectolitro'),
        ('DAL', 'Decalitro'),
        ('L', 'Litro'),
        ('DL', 'Decilitro'),
        ('CL', 'Centilitro'),
        ('ML', 'Mililitro'),
    ]
    
    nombre = models.CharField(max_length=255)
    marca = models.ForeignKey('gestionar_marca.Marca', on_delete=models.CASCADE)
    presentacion = models.ForeignKey('gestionar_presentacion.Presentacion', on_delete=models.CASCADE, null=False)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey('gestionar_categoria.Categoria', on_delete=models.CASCADE)
    proveedor = models.ForeignKey('gestionar_proveedor.Proveedor', on_delete=models.CASCADE)


    precio = models.DecimalField(max_digits=50, decimal_places=2, validators=[MinValueValidator(0)])
    unidad_de_medida = models.CharField(max_length=50, choices=UNIDADES_MEDIDA)
    
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

    def clean(self):
        super().clean()
        if self.presentacion_id is not None and not self.presentacion.estado:
            raise ValidationError("No se puede asignar una presentación inactiva a un producto.")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)