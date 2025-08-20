from django.urls import path
from account.views import login, register, redefinir_senha, logout


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('redefinir_senha/', redefinir_senha, name='redefinir_senha'),
    path('logout/', logout, name='logout'),
]