# Generated by Django 4.1.4 on 2023-05-30 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr001_ser', models.IntegerField(null=True, unique=True, verbose_name='Serial Atrol Colaborador')),
                ('usr001_nome', models.CharField(max_length=60, null=True, verbose_name='Nome do Colaborador')),
                ('usr001_email', models.CharField(max_length=100, null=True, verbose_name='Email do Colaborador')),
                ('usr001_cpf', models.CharField(max_length=11, null=True, unique=True, verbose_name='CPF do Colaborador')),
                ('usr001_tipo', models.CharField(max_length=1, null=True, verbose_name='Tipo de perfil Atrol')),
                ('usr001_perfil', models.IntegerField(null=True, verbose_name='Serial Perfil Atrol')),
                ('usr001_ativo', models.BooleanField(null=True, verbose_name='Indicador de Atividade Atrol')),
                ('usr001_stt', models.IntegerField(null=True, verbose_name='Serial STT')),
                ('usr001_scr', models.IntegerField(null=True, verbose_name='Serial SCR')),
                ('emp010_ser', models.IntegerField(null=True, verbose_name='Serial emp010_ser')),
                ('emp006_ser', models.IntegerField(null=True, verbose_name='Serial emp006_ser')),
                ('emp004_ser', models.IntegerField(null=True, verbose_name='Serial emp004_ser')),
                ('emp005_ser', models.IntegerField(null=True, verbose_name='Serial emp005_ser')),
                ('emp003_ser', models.IntegerField(null=True, verbose_name='Serial emp003_ser')),
                ('cli004_ser', models.IntegerField(null=True, verbose_name='Serial cli004_ser')),
                ('emp002_ser', models.IntegerField(null=True, verbose_name='Serial emp002_ser')),
                ('emp003_sigla', models.CharField(max_length=10, null=True, verbose_name='Sigla da Cidade')),
                ('emp003_nome', models.CharField(max_length=225, null=True, verbose_name='Nome Cidade')),
                ('loc003_ser', models.IntegerField(null=True, verbose_name='Serial loc003_ser')),
                ('emp012_ser', models.IntegerField(null=True, verbose_name='Serial emp012_ser')),
                ('emp011_ser', models.IntegerField(null=True, verbose_name='Serial emp011_ser')),
                ('usr007_supervisor', models.IntegerField(null=True, verbose_name='Serial usr007_supervisor')),
                ('datanow', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]