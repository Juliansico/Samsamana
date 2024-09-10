from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import Usuario

class UsuarioForm(UserCreationForm):
    ROL_CHOICES = [
        ('administrador', 'Administrador'),
        ('empleado', 'Empleado'),
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
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'})
    )
    telefono = forms.CharField(
        label="Teléfono",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'})
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
        fields = ['username', 'apellido', 'tipo_documento', 'documento', 'telefono', 'email', 'password1', 'password2', 'rol_usuario', 'estado']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-3'})
        self.fields['estado'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['tipo_documento'].widget.attrs.update({'class': 'form-select mb-3'})
        self.fields['rol_usuario'].widget.attrs.update({'class': 'form-select mb-3'})

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.replace(' ', '').isalpha():
            raise forms.ValidationError("El nombre solo debe contener letras.")
        return username

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if not apellido.replace(' ', '').isalpha():
            raise forms.ValidationError("El apellido solo debe contener letras.")
        return apellido

    def clean_documento(self):
        documento = self.cleaned_data.get('documento')
        if not documento.isdigit() or len(documento) > 10:
            raise forms.ValidationError("El documento debe contener solo números y tener máximo 10 dígitos.")
        return documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit() or len(telefono) > 10:
            raise forms.ValidationError("El teléfono debe contener solo números y tener máximo 10 dígitos.")
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya está registrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            usuario.set_password(password)
        usuario.is_superuser = False
        usuario.is_staff = False
        if commit:
            usuario.save()
            rol_usuario = self.cleaned_data.get('rol_usuario')
            group = Group.objects.get(name=rol_usuario)
            usuario.groups.add(group)
        return usuario