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

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya existe")
        return username

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario
