from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def redefinir_senha(request):
    return render(request, 'accounts/recover_password.html')

def logout(request):
    return render(request, 'logout.html')