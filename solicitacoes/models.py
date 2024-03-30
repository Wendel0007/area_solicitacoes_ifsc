from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .utils import upload_to


class TipoSolicitacao(models.Model):
    nome_completo = models.CharField(max_length=255, null=True, verbose_name="Tipo de Solicitação")
    data_cadastro = models.DateTimeField(auto_now_add=True)


class Solicitacao(models.Model):
    STATUS_CHOICES = [
        ('aprovado', 'Aprovado'),
        ('em_analise', 'Em Analise'),
        ('negado', 'Negado'),
        ('cancelado', 'Cancelado'),
    ]
    tipo_solicitacao = models.ForeignKey(TipoSolicitacao, on_delete=models.CASCADE)
    descricao = models.TextField(null=False, blank=False, verbose_name="Descrição da Solicitação")
    arquivo = models.ImageField(
        upload_to=upload_to,
        null=False, blank=False
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='em_analise',
        verbose_name="Status da Solicitação"
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
