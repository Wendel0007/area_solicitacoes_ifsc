# Generated by Django 5.0.3 on 2024-03-29 17:30

import solicitacoes.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes', '0003_alter_solicitacao_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='arquivo',
            field=models.ImageField(upload_to=solicitacoes.utils.upload_to),
        ),
    ]
