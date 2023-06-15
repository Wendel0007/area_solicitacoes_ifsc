# Generated by Django 4.1.4 on 2023-06-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutosCantina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Nome Produto')),
                ('descricao', models.TextField(max_length=225, verbose_name='Descrição Produto')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo Produto')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Valor Produto')),
                ('imagem', models.ImageField(upload_to='imagens-itens-cantina/', verbose_name='Imagem Produto')),
                ('status', models.BooleanField(default=True, verbose_name='Status Produto')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data Criação Produto')),
            ],
        ),
    ]
