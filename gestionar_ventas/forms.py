from django import forms
from .models import Venta, DetalleVenta
from django.core.exceptions import ValidationError

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['usuario']  # Asegúrate de incluir los campos necesarios
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_usuario(self):
        usuario = self.cleaned_data.get('usuario')
        if not usuario:
            raise ValidationError("Es obligatorio seleccionar un usuario.")
        return usuario


class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')

        # Verificar que los campos no estén vacíos
        if not producto:
            raise ValidationError("Es obligatorio seleccionar un producto.")
        if not cantidad:
            raise ValidationError("Es obligatorio especificar una cantidad.")
        
        # Validar que la cantidad sea mayor a 0
        if cantidad <= 0:
            raise ValidationError("La cantidad debe ser un número mayor que cero.")
        
        # Validación del stock
        if producto and producto.stock < cantidad:
            raise ValidationError(f"Stock insuficiente. Solo hay {producto.stock} unidades disponibles.")
        return cleaned_data