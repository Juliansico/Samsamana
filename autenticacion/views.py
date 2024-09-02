from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse_lazy
from .forms import FormularioRegistro 
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth import get_user_model
import logging
logger = logging.getLogger(__name__)

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registrar(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = FormularioRegistro()
    return render(request, 'registrar_usuario.html', {'form': formulario})

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'restablecer_contrasena.html'
    success_url = reverse_lazy('reset_password_complete')

    def form_valid(self, form):
        uidb64 = self.kwargs.get('uidb64')  
        user = self.get_user(uidb64)
        if user is not None:
            user.set_password(form.cleaned_data['new_password1'])
            user.reset_token = ''  
            user.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_user(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user