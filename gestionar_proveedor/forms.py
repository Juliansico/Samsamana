from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Proveedor
from gestionar_usuarios.models import Usuario

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

class UsuarioForm(UserCreationForm, BaseModelForm):
    ROL_CHOICES = [
        ('empleado', 'Empleado'),
    ]
    
    rol_usuario = forms.ChoiceField(choices=ROL_CHOICES)
    tipo_documento = forms.ChoiceField(
        choices=Usuario.TIPO_DOCUMENTO_CHOICES,
        label="Tipo de documento"
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuario
        fields = ['username', 'apellido', 'tipo_documento', 'documento', 'telefono', 'email', 'estado']
        widgets = {
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya está registrado.")
        return email

class ProveedorForm(BaseModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'email', 'estado']
        widgets = {
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }