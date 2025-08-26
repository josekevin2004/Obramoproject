from django.shortcuts import render, redirect
from account.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

# Create your views here.
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
          nome_usuario = form['login'].value()
          senha = form['password'].value()

        if nome_usuario == '' or senha == '':
              messages.error(request, 'Todos os campos são obrigatórios!')
              return redirect('login')

        credenciais_usuario = auth.authenticate(
              request,
              username = nome_usuario,
              password = senha,
           )     

        if credenciais_usuario == None:
              messages.error(request, 'Login falhou! tente novamente')
              return render(request, 'accounts/login.html', {'form': form})
          
        auth.login(request, credenciais_usuario)
        return redirect('dashboard')


    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            nome_usuario = form['login'].value().strip()
            email_usuario = form['email'].value().strip()
            senha = form['password'].value().strip()
            confirma_senha = form['reverter_password'].value().strip()

            if nome_usuario == '' or email_usuario == '' or senha == '' or confirma_senha == '':
                return redirect('register')
            
            if senha != confirma_senha:
                messages.error(request, 'As senhas não coincidem')
                return redirect('register')
            
            user_exists = User.objects.filter(username=nome_usuario).exists()
            email_exists = User.objects.filter(email=email_usuario).exists()

            if user_exists:
                messages.error(request, 'Já existe um usuário com este nome')
                return render(request, '')
            
            if email_exists:
                messages.error(request, 'Este e-mail já esta cadastrado')
                return redirect('register')
            
            meu_user = User.objects.create_user(
                username=nome_usuario,
                email=email_usuario,
                password=senha
            )

            meu_user.save()
            
            messages.success(request, 'Usuário cadastrado com sucesso!')     
    return render(
        request,
        'accounts/register.html',
        {'form': form, 'mensagens': messages.get_messages(request)}
    )
from django.contrib import messages

def recover_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            # Aqui você pode implementar o envio de e-mail real
            messages.success(request, 'Se o e-mail estiver cadastrado, você receberá instruções para redefinir a senha.')
        else:
            messages.error(request, 'Informe um e-mail válido.')
    return render(request, 'accounts/recover_password.html')

def logout(request):
    auth_logout(request)
    return redirect('inicio')