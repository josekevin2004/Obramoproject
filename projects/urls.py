from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='home'), 
    path('inicio/', views.inicio, name='inicio'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profissionais/', views.profissionais, name='profissionais'),
    path('mensagens/', views.mensagens, name='mensagens'),
    path('pagamento/', views.pagamento, name='pagamento'),
    path('avaliacao/', views.avaliacao, name='avaliacao'),
    path('perfil/', views.perfil, name='perfil'),
    path('meusprojetos/', views.meusprojetos, name='meusprojetos'),
    path('inicioP/', views.inicioP, name='inicioP'),
    path('clientesP/', views.clientesP, name='clientesP'),
    path('dashboardP/', views.dashboardP, name='dashboardP'),
    path('mensagensP/', views.mensagensP, name='mensagensP'),
    path('meusprojetosP/', views.meusprojetosP, name='meusprojetosP'),
    path('pagamentoP/', views.pagamentoP, name='pagamentoP'),
    path('perfilP/', views.perfilP, name='perfilP'),
    path('procurarprojetosP/', views.procurarprojetosP, name='procurarprojetosP'),
]
