from django import forms
from django.contrib.auth.models import User

from painel_cantina.models import ProdutosCantina


class ProdutosCantinaForm(forms.ModelForm):
    class Meta:
        model = ProdutosCantina
        fields = ["titulo", "descricao", "tipo", "valor", "imagem"]

    TIPO_PRODUTO = (
        ('1', 'Bebida'),
        ('2', 'Salgado'),
        ('3', 'Doce'),
        ('4', 'Outros'),
    )

    titulo = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Nome do Produto'}),
        error_messages={'required': 'Nome do Produto não pode ser vazio'},
        label='Nome do Produto'
    )
    descricao = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Descrição do Produto'}),
        error_messages={'required': 'Descrição do Produto não pode ser vazio'},
        label='Descrição do Produto'
    )
    tipo = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control', 'placeholder': 'Tipo do Produto'}),
        error_messages={'required': 'Tipo do Produto não pode ser vazio'},
        label='Tipo do Produto',
        choices=TIPO_PRODUTO
    )
    valor = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Valor do Produto'}),
        error_messages={'required': 'Valor do Produto não pode ser vazio'},
        label='Valor do Produto'
    )
    imagem = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control', 'placeholder': 'Imagem do Produto'}),
        error_messages={'required': 'Imagem do Produto não pode ser vazio'},
        label='Imagem do Produto'
    )


class EditarProdutosCantinaForm(forms.ModelForm):
    class Meta:
        model = ProdutosCantina
        fields = ["titulo", "descricao", "tipo", "valor", "imagem", "status"]

    TIPO_PRODUTO = (
        ('1', 'Bebida'),
        ('2', 'Salgado'),
        ('3', 'Doce'),
        ('4', 'Outros'),
    )
    STATUS_PRODUTO = (
        ('True', 'Ativo'),
        ('False', 'Desativo'),
    )

    titulo = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Nome do Produto'}),
        error_messages={'required': 'Nome do Produto não pode ser vazio'},
        label='Nome do Produto'
    )
    descricao = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Descrição do Produto'}),
        error_messages={'required': 'Descrição do Produto não pode ser vazio'},
        label='Descrição do Produto'
    )
    tipo = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control', 'placeholder': 'Tipo do Produto'}),
        error_messages={'required': 'Tipo do Produto não pode ser vazio'},
        label='Tipo do Produto',
        choices=TIPO_PRODUTO
    )
    valor = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Valor do Produto'}),
        error_messages={'required': 'Valor do Produto não pode ser vazio'},
        label='Valor do Produto'
    )
    imagem = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control', 'placeholder': 'Imagem do Produto'}),
        error_messages={'required': 'Imagem do Produto não pode ser vazio'},
        label='Imagem do Produto'
    )
    status = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control', 'placeholder': 'Status do Produto'}),
        error_messages={'required': 'Status do Produto não pode ser vazio'},
        label='Status do Produto',
        choices=STATUS_PRODUTO
    )
