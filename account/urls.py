from django.urls import path
from account.views import login, register, recover_password, logout


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('recover_password/', recover_password, name='recover_password'),
    path('logout/', logout, name='logout'),
]