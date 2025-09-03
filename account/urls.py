from django.urls import path
from account.views import login, register, recover_password, logout
from account import views

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('recover_password/', recover_password, name='recover_password'),
    path('logout/', logout, name='logout'),

    # Dashboards
    path('dashboard/cliente/', views.dashboard, name='dashboard'),
    path('dashboard/profissional/', views.dashboardP, name='dashboardP'),
]
