import psycopg2
import psycopg2.extras
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import LoginForm, PasswordChangeCustomForm, UserRegistrationForm


@login_required
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard/components/index.html')


def login_form(request):
    usuario_autenticado = request.user.is_authenticated
    if usuario_autenticado:
        return redirect('dashboard')

    formulario = LoginForm()
    context = {'formulario': formulario}
    return render(request, 'dashboard/auth/login.html', context=context)


def login_action(request):
    if not request.POST:
        raise Http404()

    formulario = LoginForm(request.POST)

    if formulario.is_valid():
        username = formulario.cleaned_data.get('username')
        password = formulario.cleaned_data.get('password')
        usuario_autenticado = authenticate(
            username=username, password=password)

        if usuario_autenticado:
            login(request, usuario_autenticado)
            messages.success(request, 'Usuário logado com sucesso')
            return redirect('dashboard')

    messages.error(request, 'Usuário ou Senha inválido(a)')
    return redirect('login_form')


def registerUser(request):
    if request.method == 'GET':

        formulario = UserRegistrationForm()
        context = {'formCpf': formulario}

        return render(request, 'dashboard/auth/cadastro.html', context=context)

    if request.method == 'POST':
        formUser = UserRegistrationForm(request.POST)
        if formUser.is_valid():
            user = formUser.save(commit=False)
            user.set_password(request.POST.get('password1'))
            user.save()

            messages.success(
                request, f"Usuário cadastrado!")
            return redirect('login_form')
        else:
            messages.error(
                request, "Usuário informado contém algum problema ou já existe. Abra um chamado para o SUPORTE TÉCNICO, informando o problema encontrado e seu CPF.")
            if not formUser.is_valid():
                print(formUser.errors)  # Exibir erros do UserRegistrationForm
            return redirect('login_form')


def logout_action(request):
    logout(request)
    return redirect('login_form')


@login_required
def altera_senha(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('dashboard')
    else:
        form = PasswordChangeCustomForm(user=request.user)
    return render(request, 'dashboard/auth/altera_senha.html', {'form': form})
