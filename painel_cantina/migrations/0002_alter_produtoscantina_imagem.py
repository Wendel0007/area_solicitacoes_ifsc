# Generated by Django 4.1.4 on 2023-06-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel_cantina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtoscantina',
            name='imagem',
            field=models.ImageField(null=True, upload_to='imagens-itens-cantina/', verbose_name='Imagem Produto'),
        ),
    ]
