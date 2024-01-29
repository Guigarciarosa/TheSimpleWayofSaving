from django.shortcuts import render, redirect
from .forms import UsuarioRegistrationForm
# Create your views here.

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecione para a página desejada após o cadastro
            return redirect('página_de_sucesso')
    else:
        form = UsuarioRegistrationForm()

    return render(request, 'cadastrar_usuario.html', {'form': form})