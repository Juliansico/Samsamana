from django import forms
from .models import Proveedor
from django.core.exceptions import ValidationError
import re

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class ProveedorForm(BaseModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'email']
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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Este campo es obligatorio.")
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValidationError("Por favor, ingrese un correo electrónico válido.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        email = cleaned_data.get('email')

        # Verificación de duplicados
        if Proveedor.objects.filter(nombre=nombre).exists() and not self.instance.pk:
            raise ValidationError("Ya existe un proveedor con este nombre.")
        
        if Proveedor.objects.filter(email=email).exists() and not self.instance.pk:
            raise ValidationError("Ya existe un proveedor con este correo electrónico.")

        return cleaned_data
