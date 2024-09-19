from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import  Producto
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError





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





from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Producto
from decimal import Decimal
from gestionar_presentacion.models import Presentacion
from gestionar_marca.models import Marca
from gestionar_categoria.models import Categoria
from gestionar_proveedor.models import Proveedor

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex='^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message='El nombre solo puede contener letras y espacios.',
                code='invalid_name'
            )
        ]
    )
    precio = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'presentacion', 'proveedor', 'categoria', 'precio', 'unidad_de_medida', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-check-input'})
        
        # Filtrar solo presentaciones, marcas y categorías activas
        self.fields['presentacion'].queryset = Presentacion.objects.filter(estado=True)
        self.fields['marca'].queryset = Marca.objects.filter(estado=True)
        self.fields['categoria'].queryset = Categoria.objects.filter(estado=True)
        self.fields['proveedor'].queryset = Proveedor.objects.filter(estado=True)

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        try:
            # Removemos los puntos de los miles y reemplazamos la coma por punto
            precio_limpio = precio.replace('.', '').replace(',', '.')
            precio_decimal = Decimal(precio_limpio)
            if precio_decimal < 0:
                raise ValidationError("El precio no puede ser negativo.")
            return precio_decimal
        except:
            raise ValidationError("Por favor, ingrese un precio válido.")