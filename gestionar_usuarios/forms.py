from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import Usuario

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

class UsuarioForm(UserCreationForm):
    ROL_CHOICES = [
        ('Productos', 'Productos'),
        ('Ventas', 'Ventas'),
        ('Presentacion', 'Presentacion'),
        ('Marca', 'Marca'),
        ('Categoria', 'Categoria'),
        ('Proveedor', 'Proveedor'),
        ('Compras', 'Compras'),
    ]
    
    rol_usuario = forms.ChoiceField(choices=ROL_CHOICES, label="Rol de usuario", required=True)
    tipo_documento = forms.ChoiceField(
        choices=Usuario.TIPO_DOCUMENTO_CHOICES,
        label="Tipo de documento",
        required=True
    )
    documento = forms.CharField(
        label="Número de documento",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telefono = forms.CharField(
        label="Teléfono",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Usuario
        fields = ['username', 'apellido', 'tipo_documento', 'documento', 'telefono', 'email', 'estado']
        widgets = {
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya está registrado.")
        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            usuario.set_password(password)
        usuario.is_superuser = False
        usuario.is_staff = False  # Change this to False
        if commit:
            usuario.save()
            rol_usuario = self.cleaned_data.get('rol_usuario')
            group = Group.objects.get(name=rol_usuario)
            usuario.groups.add(group)
        return usuario