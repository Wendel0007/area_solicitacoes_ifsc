from django.db import models


class ProdutosCantina(models.Model):
    titulo = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Nome Produto")
    descricao = models.TextField(
        max_length=225, null=False, blank=False, verbose_name="Descrição Produto")
    tipo = models.CharField(max_length=100, null=False,
                            blank=False, verbose_name="Tipo Produto")
    valor = models.DecimalField(
        null=False, max_digits=5, decimal_places=2, verbose_name="Valor Produto")
    imagem = models.ImageField(
        null=True, blank=False, upload_to='imagens-itens-cantina/', verbose_name="Imagem Produto")

    status = models.BooleanField(default=True, verbose_name="Status Produto")
    data_criacao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data Criação Produto")

    def __str__(self):
        return f"{self.id} - {self.titulo}"

    def save(self, *args, **kwargs):
        # Verifica se o objeto já foi salvo antes de acessar a propriedade imagem
        if not self.pk:
            super().save(*args, **kwargs)

        # Realiza o processamento da imagem, como renomear o arquivo
        # Agora você pode acessar self.imagem.path sem problemas

        super().save(*args, **kwargs)
