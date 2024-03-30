from django.urls import path

from . import views

urlpatterns = [
    path('solicitacoes/', views.painelSolicitacoes, name='painelSolicitacoes'),
    path('nova-solicitacao/', views.novaSolicitacao, name='novaSolicitacao'),
    path('painel-aprovacao-solicitacoes/', views.painelAprovacaoSolicitacoes, name='painelAprovacaoSolicitacoes'),
    path('aprovacao-solicitacao/<int:id>', views.aprovacaoSolicitacao, name='aprovacaoSolicitacao'),
    path('deletar-solicitacao/<int:id>', views.deletarSolicitacao, name='deletarSolicitacao'),
]
