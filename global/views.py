from django.shortcuts import render
from django.contrib.auth import authenticate, login, AuthenticationForm
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/success_url/')  # Redirige a la URL de éxito
        else:
            form = AuthenticationForm(request.POST)
            form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})