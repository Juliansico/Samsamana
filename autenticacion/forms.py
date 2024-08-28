from django import forms
from gestionar_usuarios.models import Usuario

class FormularioRegistro(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')
    
    class Meta:
        model = Usuario
        fields = ['username', 'apellido', 'email', 'tipo_documento', 'documento', 'telefono']
        labels = {
            'username': 'Nombre de usuario',
            'apellido': 'Apellido',
            'email': 'Correo electrónico',
            'tipo_documento': 'Tipo de documento',
            'documento': 'Número de documento',
            'telefono': 'Teléfono',
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Las contraseñas no coinciden")

        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya existe")
        return username

    def save(self, commit=True):
        usuario = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            usuario.set_password(password)
        if commit:
            usuario.save()
        return usuario

# Formulario para recuperación de contraseña
class RecuperarContrasenaForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')

class RestablecerContrasenaForm(forms.Form):
    nueva_contrasena = forms.CharField(widget=forms.PasswordInput(), label='Nueva contraseña')
    confirmacion_contrasena = forms.CharField(widget=forms.PasswordInput(), label='Confirmar contraseña')
    
    def clean(self):
        cleaned_data = super().clean()
        nueva_contrasena = cleaned_data.get('nueva_contrasena')
        confirmacion_contrasena = cleaned_data.get('confirmacion_contrasena')

        if nueva_contrasena and confirmacion_contrasena and nueva_contrasena != confirmacion_contrasena:
            self.add_error('confirmacion_contrasena', 'Las contraseñas no coinciden.')

        return cleaned_data