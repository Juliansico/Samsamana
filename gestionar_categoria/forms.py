from django import forms
from .models import Categoria
from django.core.exceptions import ValidationError
import re

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
        # Eliminar la referencia al campo 'estado' en caso de que no exista
        if 'estado' in self.fields:
            self.fields['estado'].widget.attrs.update({
                'class': 'form-check-input',
                'style': 'width: 20px; height: 20px;'
            })

class CategoriaForm(BaseModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']  # Eliminamos 'estado' de los fields
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio.',
            },
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError("Este campo es obligatorio.")
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise ValidationError("El nombre solo puede contener letras y espacios.")
        if Categoria.objects.filter(nombre__iexact=nombre).exists():
            raise ValidationError("Ya existe una categoría con este nombre.")
    
        return nombre
