from django import forms
from .models import Proveedor
from django.core.exceptions import ValidationError
import re

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        self.fields['estado'].widget.attrs.update({
            'class': 'form-check-input',
            'style': 'width: 20px; height: 20px;'
        })

class ProveedorForm(BaseModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'email', 'estado']
        widgets = {
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'nombre': {'required': 'Este campo es obligatorio.'},
            'direccion': {'required': 'Este campo es obligatorio.'},
            'telefono': {'required': 'Este campo es obligatorio.'},
            'email': {'required': 'Este campo es obligatorio.'},
        }
        
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError("Este campo es obligatorio.")
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre

    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if not direccion:
            raise ValidationError("Este campo es obligatorio.")
        return direccion

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Este campo es obligatorio.")
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValidationError("Por favor, ingrese un correo electrónico válido.")
        return email

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono:
            raise ValidationError("Este campo es obligatorio.")
        if not re.match(r'^\d{10}$', telefono):
            raise ValidationError("El teléfono debe contener exactamente 10 dígitos.")
        return telefono