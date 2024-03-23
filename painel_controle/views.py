import os
import pdb

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.http import Http404
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode

from .forms import (LoginForm, PasswordChangeCustomForm, PerfilForm,
                    ResetPassForm, UserRegistrationForm)
from .models import Curso
from .utils import send_email_first


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
            if usuario_autenticado.is_active:
                login(request, usuario_autenticado)
                messages.success(request, 'Usuário logado com sucesso')
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuário desativado')
        else:
            messages.error(request, 'Usuário ou Senha inválido(a)')
    else:
        messages.error(request, 'Formulário inválido(a)')

    return redirect('login_form')


def registerUser(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()

        formulario = UserRegistrationForm()
        context = {
            'formCpf': formulario,
            'cursos': cursos,
        }

        return render(request, 'dashboard/auth/cadastro.html', context=context)

    if request.method == 'POST':
        formUser = UserRegistrationForm(request.POST)
        formPerfil = PerfilForm(request.POST)

        if formUser.is_valid() and formPerfil.is_valid():
            email_inicial = formUser.cleaned_data.get('email_inicial')
            dominio = formUser.cleaned_data.get('dominio')
            email = f"{email_inicial}{dominio}"
            # pdb.set_trace()

            user = formUser.save(commit=False)
            user.email = email
            user.set_password(request.POST.get('password1'))
            user.save()

            perfil = formPerfil.save(commit=False)
            perfil.user = user
            perfil.save()

            send_email_first(
                'NÃO RESPONDA - Cadastro de usuario IFSC', 'Cadastro confirmado no Portal IFSC Campus Caçador', email)

            messages.success(
                request, f"Usuário cadastrado!")
            return redirect('login_form')
        else:
            messages.error(
                request, "Usuário informado contém algum problema ou já existe.")
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


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Redefinição de senha Portal Campus Caçador"
                    email_template_name = "dashboard/auth/emails/email_recuperacao_senha.html"
                    content = {
                        "email": user.email,
                        'domain': f'{os.getenv("BASE_URL")}',
                        'site_name': 'Portal Campus Caçador',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                    }
                    html_content = render_to_string(email_template_name, content)
                    text_content = strip_tags(html_content)
                    mail = EmailMultiAlternatives(
                        subject, text_content, f'{os.getenv("EMAIL_HOST_USER")}', [user.email])
                    mail.attach_alternative(html_content, 'text/html')
                    mail.send()
                return redirect("password_reset_done")
            else:
                messages.error(
                    request, 'O email informado, não existe em nossa base de dados. Verifique se informou corretamente ou faça um novo cadastro.')
                return redirect("reset_password")
        else:
            messages.error(
                request, 'O email informado, não existe em nossa base de dados. Verifique se informou corretamente ou faça um novo cadastro.')
            return redirect("reset_password")
    password_reset_form = ResetPassForm()
    return render(request=request, template_name="dashboard/auth/password_reset.html", context={"form": password_reset_form})
