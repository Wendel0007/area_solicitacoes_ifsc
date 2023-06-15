from django.urls import path

from . import views

urlpatterns = [
    path('painel_cantina/', views.painelCantina, name='painel_cantina'),

    path('novo_produto_cantina/', views.NovoProdutoCantina,
         name='novo_produto_cantina'),

    path('listar_produto_cantina/', views.listarProdutoCantina,
         name='listar_produto_cantina'),

    path('listar_produto_cantina/editar_produto/<int:id>', views.EditarProdutoCantina,
         name='editar_produto'),

    path('listar_produto_cantina/deletar_produto/<int:id>', views.DeletarProdutoCantina,
         name='deletar_produto'),
]
