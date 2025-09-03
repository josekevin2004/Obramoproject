from django.shortcuts import render, redirect
from account.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import logout as auth_logout
from account.models import Profile

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            nome_usuario = form['login'].value()
            senha = form['password'].value()

            if not nome_usuario or not senha:
                messages.error(request, 'Todos os campos são obrigatórios!')
                return redirect('login')

            credenciais_usuario = auth.authenticate(
                request,
                username=nome_usuario,
                password=senha,
            )

            if credenciais_usuario is None:
                messages.error(request, 'Login falhou! tente novamente')
                return render(request, 'accounts/login.html', {'form': form})

            auth.login(request, credenciais_usuario)

            # Busca tipo de usuário
            profile = Profile.objects.get(user=credenciais_usuario)
            if profile.user_type == "client":
                return redirect('dashboard')
            else:
                return redirect('dashboardP')

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
            user_type = form['user_type'].value()

            if not nome_usuario or not email_usuario or not senha or not confirma_senha:
                messages.error(request, 'Preencha todos os campos.')
                return redirect('register')

            if senha != confirma_senha:
                messages.error(request, 'As senhas não coincidem')
                return redirect('register')

            if User.objects.filter(username=nome_usuario).exists():
                messages.error(request, 'Já existe um usuário com este nome')
                return redirect('register')

            if User.objects.filter(email=email_usuario).exists():
                messages.error(request, 'Este e-mail já está cadastrado')
                return redirect('register')

            # Cria usuário
            meu_user = User.objects.create_user(
                username=nome_usuario,
                email=email_usuario,
                password=senha
            )
            meu_user.save()

            # Cria perfil
            Profile.objects.create(user=meu_user, user_type=user_type)

            # Mensagem de sucesso, mas não redireciona
            messages.success(request, 'Usuário cadastrado com sucesso! Agora faça login para acessar a dashboard.')

    return render(request, 'accounts/register.html', {'form': form})


def recover_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            messages.success(request, 'Se o e-mail estiver cadastrado, você receberá instruções para redefinir a senha.')
        else:
            messages.error(request, 'Informe um e-mail válido.')
    return render(request, 'accounts/recover_password.html')


def logout(request):
    auth_logout(request)
    return redirect('inicio')


# Dashboards
def dashboard(request):
    return render(request, 'projects/cliente/dashboard.html')


def dashboardP(request):
    return render(request, 'projects/profissional/dashboardP.html')
