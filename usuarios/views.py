from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario

def login_view(request):
    if request.user.is_authenticated:
        return redirect('inicio')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
            
    return render(request, 'usuarios/login.html')

def registro_view(request):
    if request.user.is_authenticated:
        return redirect('inicio')
        
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'usuarios/registro.html')
            
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este correo ya está registrado.')
            return render(request, 'usuarios/registro.html')
            
        try:
            # We use email as the username under the hood
            user = Usuario.objects.create_user(username=email, email=email, password=password, first_name=nombre)
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('inicio')
        except Exception as e:
            messages.error(request, f'Ocurrió un error al registrar: {str(e)}')
            
    return render(request, 'usuarios/registro.html')

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def perfil_config(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        foto = request.FILES.get('foto')
        
        user = request.user
        if nombre:
            user.first_name = nombre
        if foto:
            user.foto_perfil = foto
        user.save()
        messages.success(request, 'Configuración actualizada correctamente.')
        return redirect('inicio')
        
    return render(request, 'usuarios/perfil_config.html')
