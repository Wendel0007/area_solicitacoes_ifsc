from django.urls import path

from . import views

# Importa as views que a gente criou
# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('relDespesasViagens/', views.relDespesasViagens,
    #      name='relDespesasViagens'),

    path('login/action/', views.login_action, name='login_action'),

    path('cadastro/action/', views.registerUser, name='cadastro_action'),
    path('logout/action/', views.logout_action, name='logout_action'),
    path('login/', views.login_form, name='login_form'),

    path('alterar-senha-acesso/', views.altera_senha, name='altera_senha'),
]
