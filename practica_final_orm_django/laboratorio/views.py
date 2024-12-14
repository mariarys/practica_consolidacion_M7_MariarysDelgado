from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Laboratorio
from .forms import LaboratorioForm, CustomUserCreationForm


def index(request):
    return render(request, 'index.html')


@login_required
def informacion_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'informacion_laboratorio.html', {'laboratorios': laboratorios})


@login_required
def agregar_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡El laboratorio se ha creado exitosamente!")
            return redirect('informacion_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'agregar_laboratorio.html', {'form': form})

@login_required
def editar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Laboratorio actualizado!")
            return redirect('informacion_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'editar_laboratorio.html', {'form': form})


@login_required
def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
    if request.method == 'POST':
        laboratorio.delete()
        messages.success(request, 'El laboratorio ha sido eliminado con éxito.')
        return redirect('informacion_laboratorios')
    return render(request, 'eliminar_laboratorio.html', {'laboratorio': laboratorio})


def ingresar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡El usuario se ha registrado exitosamente!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'ingresar_usuario.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido {username}!')
            return redirect('index')
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('index')
