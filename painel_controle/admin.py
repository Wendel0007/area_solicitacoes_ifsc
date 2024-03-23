from django.contrib import admin

from .models import Curso, Perfil


# Register your models here.
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_completo', 'cpf',
                    'matricula', 'user', 'data_cadastro']
    list_display_links = ['id', 'nome_completo',
                          'cpf', 'matricula', 'user', 'data_cadastro']
    search_fields = ['id', 'nome_completo', 'cpf',
                     'matricula', 'user', 'data_cadastro']
    list_per_page = 20
    ordering = ['-id']


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_completo', 'tipo_curso', 'data_cadastro']
    list_display_links = ['id', 'nome_completo', 'tipo_curso', 'data_cadastro']
    search_fields = ['id', 'nome_completo', 'tipo_curso', 'data_cadastro']
    list_per_page = 20
    ordering = ['-id']
