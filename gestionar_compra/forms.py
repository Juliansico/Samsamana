from django import forms
from .models import Compra, DetalleCompra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['usuario', 'estado']  # Elimina 'fecha' porque no es editable
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        
class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad', 'proveedor', 'precio']  # Incluir 'precio'
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Opcionalmente, puedes establecer el precio como solo lectura aquí también
        self.fields['precio'].disabled = True  # Esto asegura que no sea editable en el formulario
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['proveedor'].widget.attrs.update({'readonly': True})