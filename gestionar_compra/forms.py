from django import forms
from .models import Compra, DetalleCompra
from django.core.exceptions import ValidationError

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['usuario', 'estado']  # Eliminamos 'fecha' porque no es editable
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad', 'precio']  # El campo 'precio' será editable
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),  # Hacemos el campo de precio editable
        }
        
    def clean(self):
        cleaned_data = super().clean()
        detalles = self.cleaned_data.get('detalles')
        
        # Verificar si hay detalles y si cada detalle tiene un producto seleccionado
        if detalles:
            for detalle in detalles:
                producto = detalle.get('producto')
                if not producto:
                    raise forms.ValidationError('Es obligatorio seleccionar un producto para cada detalle de la compra.')
        
        return cleaned_data
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is None or cantidad <= 0:
            raise ValidationError("La cantidad debe ser un número entero mayor que cero.")
        return cantidad

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None or precio <= 0:
            raise ValidationError("El precio debe ser un número mayor que cero.")
        return precio