# Generated by Django 5.0.3 on 2024-03-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel_controle', '0004_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='numero_contato',
            field=models.CharField(max_length=11, null=True, verbose_name='Número para Contato'),
        ),
    ]
