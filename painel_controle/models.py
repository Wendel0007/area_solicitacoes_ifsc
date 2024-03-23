from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Curso(models.Model):
    TIPOS_CHOICES = (
        ('Técnico', 'Técnico'),
        ('Graduação', 'Graduação'),
    )
    nome_completo = models.CharField(
        max_length=255, null=True, verbose_name="Nome Curso")
    tipo_curso = models.CharField(choices=TIPOS_CHOICES,
                                  max_length=40, null=False, blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)


class Perfil(models.Model):
    nome_completo = models.CharField(
        max_length=255, null=True, verbose_name="Nome completo")
    cpf = models.CharField(max_length=14, null=True,
                           verbose_name="CPF")
    matricula = models.CharField(max_length=12, null=True,
                                 verbose_name="Matricula de estudante")

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    data_cadastro = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
