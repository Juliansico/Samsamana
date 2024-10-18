from django import forms
from .models import Marca
from django.core.exceptions import ValidationError
import re

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        if 'estado' in self.fields:
            self.fields['estado'].widget.attrs.update({
                'class': 'form-check-input',
                'style': 'width: 20px; height: 20px;'
            })

class MarcaForm(BaseModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'logoTipo']
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio.',
            },
            'logoTipo': {
                'required': 'Este campo es obligatorio.',
            },
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if Marca.objects.filter(nombre=nombre).exists() and not self.instance.pk:
            raise ValidationError("Ya existe una marca con ese nombre.")
        return nombre

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        logoTipo = cleaned_data.get("logoTipo")

        # Comprobamos si existe ya una marca con el mismo nombre y logo
        if Marca.objects.filter(nombre=nombre, logoTipo=logoTipo).exists() and not self.instance.pk:
            raise ValidationError("Ya existe una marca con este nombre y logo.")
        
        return cleaned_data
