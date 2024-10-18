from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):

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
        required=False  # Cambiado a False para que no sea requerido
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False  # Cambiado a False para que no sea requerido
    )

    class Meta:
        model = Usuario
        fields = ['username', 'apellido', 'tipo_documento', 'documento', 'telefono', 'email', 'password1', 'password2', 'estado']
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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        usuario_id = self.instance.id  # Obtener el ID del usuario actual
        if Usuario.objects.filter(username=username).exclude(id=usuario_id).exists():
            raise forms.ValidationError("El nombre de usuario ya está en uso.")
        if not username.replace(' ', '').isalpha():
            raise forms.ValidationError("El nombre solo debe contener letras.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        usuario_id = self.instance.id  # Obtener el ID del usuario actual
        if Usuario.objects.filter(email=email).exclude(id=usuario_id).exists():
            raise forms.ValidationError("El correo ya está registrado.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1 == '':
            return self.instance.password  # Retornar la contraseña existente si no hay nueva
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        if password2 == '':
            return self.instance.password  # Retornar la contraseña existente si no hay nueva
        return password2

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
            
        return usuario
