from django.contrib import admin

from .models import Solicitacao, TipoSolicitacao


# Register your models here.
@admin.register(TipoSolicitacao)
class TipoSolicitacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_completo', 'data_cadastro']
    list_display_links = ['id', 'nome_completo', 'data_cadastro']
    search_fields = ['id', 'nome_completo', 'data_cadastro']
    list_per_page = 20
    ordering = ['-id']