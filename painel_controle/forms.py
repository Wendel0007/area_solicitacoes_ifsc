from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome_completo', 'cpf', 'matricula', 'curso']


class PasswordChangeCustomForm(PasswordChangeForm):
    old_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Senha antiga'}),
        error_messages={'required': 'Senha antiga não pode ser vazia'},
        label='Senha antiga'
    )
    new_password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Nova senha'}),
        error_messages={'required': 'Nova senha não pode ser vazia'},
        label='Nova senha'
    )
    new_password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Repita a Nova senha'}),
        error_messages={'required': 'Repita a Nova senha não pode ser vazia'},
        label='Repita a Nova senha'
    )


class UserRegistrationForm(UserCreationForm):
    email_inicial = forms.CharField(max_length=100)
    dominio = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # Removido 'email' dos campos, pois será gerado dinamicamente

    def clean(self):
        cleaned_data = super().clean()
        email_inicial = cleaned_data.get('email_inicial')
        dominio = cleaned_data.get('dominio')

        # Concatena os dois campos
        email = f"{email_inicial}{dominio}"

        # Valida o e-mail
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("E-mail inválido.")

        # Adiciona o e-mail ao cleaned_data
        cleaned_data['email'] = email

        return cleaned_data

    # username = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control', 'placeholder': 'Usuario de acesso', 'oninput': 'this.value = this.value.toLowerCase();'}),
    #     error_messages={'required': 'Usuario de acesso não pode ser vazia'},
    #     label='Usuario de acesso'
    # )
    # email = forms.EmailField(
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control', 'placeholder': 'Email de acesso'}),
    #     error_messages={'required': 'Email de acesso não pode ser vazia'},
    #     label='Email de acesso'
    # )
    # password1 = forms.CharField(
    #     required=True,
    #     widget=forms.PasswordInput(attrs={
    #         'class': 'form-control', 'placeholder': 'Senha de acesso'}),
    #     error_messages={'required': 'Senha de acesso não pode ser vazia'},
    #     label='Senha de acesso'
    # )
    # password2 = forms.CharField(
    #     required=True,
    #     widget=forms.PasswordInput(attrs={
    #         'class': 'form-control', 'placeholder': 'Repita a Senha de acesso'}),
    #     error_messages={
    #         'required': 'Repita a Senha de acesso não pode ser vazia'},
    #     label='Repita a Senha de acesso'
    # )


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu usuário.'}),
        error_messages={'required': 'Usuário não pode ser vazio'},
        label='Usuário'
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
        error_messages={'required': 'Senha não pode ser vazia'},
        label='Senha'
    )


class ResetPassForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Email de acesso válido'}),
        error_messages={'required': 'Email de acesso não pode ser vazia'},
        label='Email de acesso'
    )
