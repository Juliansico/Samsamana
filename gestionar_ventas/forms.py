from django import forms
from .models import Venta, DetalleVenta


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['usuario', 'estado']  # Elimina 'fecha' porque no es editable
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio']  # Incluir 'precio'
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),  # Precio visible pero no editable
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Opcionalmente, puedes establecer el precio como solo lectura aquí también
        self.fields['precio'].disabled = True  # Esto asegura que no sea editable en el formulario


