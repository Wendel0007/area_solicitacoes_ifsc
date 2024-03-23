from django.contrib.auth import views as auth_views
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

    path('recuperar-senha-acesso/', views.password_reset_request, name='recuperar_senha'),

    path('verificar_email_recuperar_acesso/', auth_views.PasswordResetDoneView.as_view(
        template_name="dashboard/auth/password_reset_sent.html"), name="password_reset_done"),
    path('token_recuperacao_acesso/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="dashboard/auth/password_reset_form.html"), name="password_reset_confirm"),
    path('recuperacao_senha_completa/', auth_views.PasswordResetCompleteView.as_view(
        template_name="dashboard/auth/password_reset_complete.html"), name="password_reset_complete"),


]
