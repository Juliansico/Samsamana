from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import  Compra

class BaseModelForm(forms.ModelForm):
    def clean_estado(self):
        estado = self.cleaned_data['estado']
        if estado not in [True, False]:
            raise forms.ValidationError("El valor de 'estado' debe ser True o False.")
        return estado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar clase CSS común a todos los campos
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        # Personalizar el widget del campo 'estado'
        self.fields['estado'].widget.attrs.update({
            'class': 'form-check-input',
            'style': 'width: 20px; height: 20px;'
        })

class CompraForm(BaseModelForm):
    class Meta:
        model = Compra
        fields = ['fecha_Compra', 'cantidad_Producto', 'proveedor_Id', 'productos', 'total_Compra', 'estado']
        widgets = {
            'fecha_Compra': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        