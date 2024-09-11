from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Marca
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

class MarcaForm(BaseModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'logoTipo', 'estado']
        widgets = {
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio.',
            },
            'logoTipo': {
                'required': 'Este campo es obligatorio.',
            },
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError("Este campo es obligatorio.")
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise ValidationError("El nombre solo puede contener letras y espacios.")
        return nombre

    def clean_logoTipo(self):
        logoTipo = self.cleaned_data.get('logoTipo')
        if not logoTipo:
            raise ValidationError("Este campo es obligatorio.")
        return logoTipo