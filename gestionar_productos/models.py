from django.db import models
from django.core.validators import MinValueValidator

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
    presentacion = models.ForeignKey('gestionar_presentacion.Presentacion', on_delete=models.CASCADE)
    categoria = models.ForeignKey('gestionar_categoria.Categoria', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=50, decimal_places=2, validators=[MinValueValidator(0)])
    unidad_de_medida = models.CharField(max_length=50, choices=UNIDADES_MEDIDA)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre