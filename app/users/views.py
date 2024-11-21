from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from django.core.exceptions import ValidationError

from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario  # Asegúrate de importar tu modelo Usuario


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        is_superuser = request.POST.get('is_superuser')
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        sector = request.POST.get('sector', '')

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('register')

        try:
            validate_password(password1)
        except ValidationError as e:
            messages.error(request, e)
            return redirect('register')

        user = Usuario.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_superuser=is_superuser,
            password=password1,
            sector=sector
        )
        messages.success(request, "Usuario registrado exitosamente.")
        login(request, user)
        return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, "Credenciales inválidas.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')


@login_required
def user_list(request):
    users = Usuario.objects.all()  # Obtiene todos los usuarios
    return render(request, 'user_list.html', {'users': users})


@login_required
def user_list(request):
    users = Usuario.objects.all()  # Obtiene todos los usuarios
    return render(request, 'user_list.html', {'users': users})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(Usuario, id=user_id)  # Obtener el usuario por su ID
    if request.method == 'POST':
        try:
            user.username = request.POST['username']
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.is_superuser = request.POST.get('is_superuser')
            user.email = request.POST.get('email')
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            user.sector = request.POST.get('sector', '')

            if password1 != password2:
                messages.error(request, "Las contraseñas no coinciden.")
                return redirect('edit_user', user_id=user.id)

            # Si se proporciona una nueva contraseña, validarla
            if password1:
                try:
                    validate_password(password1, user)
                except ValidationError as e:
                    messages.error(request, e)
                    return redirect('edit_user', user_id=user.id)

            # Actualiza el usuario, pero solo si cambian ciertos campos
            if password1:  # Solo actualiza la contraseña si se ha proporcionado una nueva
                user.set_password(password1)
            user.save()

            messages.success(request, "Usuario actualizado exitosamente.")
            return redirect('user_list')  # Redirige al listado de usuarios

        except ValidationError as e:
            messages.error(request, e)
            return redirect('user_list')

    return render(request, 'user_edit.html', {'user': user})