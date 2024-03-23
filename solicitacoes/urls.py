from django.urls import path

from . import views

urlpatterns = [
    path('solicitacoes/', views.painelSolicitacoes, name='painelSolicitacoes'),
]
