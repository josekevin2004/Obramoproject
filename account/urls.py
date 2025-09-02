from django.urls import path
from . import views

urlpatterns = [
    # URLs de autenticação
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    # Rota adicionada para a página de recuperação de senha
    path('recover-password/', views.recover_password, name='recover_password'),

    # URLs dos Dashboards (para onde o login redireciona)
    path('dashboard/cliente/', views.dashboard_cliente, name='dashboard'),
    path('dashboard/profissional/', views.dashboard_profissional, name='dashboardP'),

    # URL da Página Inicial
    path('', views.inicio, name='inicio'),
]

