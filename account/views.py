from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from .models import Profile

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome_usuario = form.cleaned_data['login']
            senha = form.cleaned_data['password']
            
            credenciais_usuario = auth.authenticate(
                request,
                username=nome_usuario,
                password=senha,
            )

            if credenciais_usuario is not None:
                auth.login(request, credenciais_usuario)
                try:
                    profile = request.user.profile
                    if profile.user_type == 'professional':
                        # CORRIGIDO: Usando o nome da URL 'dashboardP'
                        return redirect('dashboardP') 
                    else:
                        # CORRIGIDO: Usando o nome da URL 'dashboard'
                        return redirect('dashboard')
                except Profile.DoesNotExist:
                    messages.error(request, 'Perfil de usuário não encontrado.')
                    return redirect('inicio')
            else:
                messages.error(request, 'Usuário ou senha inválidos. Tente novamente.')
                return render(request, 'accounts/login.html', {'form': form})

    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            nome_usuario = form.cleaned_data['login'].strip()
            email_usuario = form.cleaned_data['email'].strip()
            senha = form.cleaned_data['password'].strip()
            confirma_senha = form.cleaned_data['reverter_password'].strip()

            def render_error(message):
                # Função auxiliar para renderizar a página com erro e um formulário limpo
                messages.error(request, message)
                form = RegisterForm() # Cria uma nova instância vazia do formulário
                return render(request, 'accounts/register.html', {'form': form})

            if senha != confirma_senha:
                return render_error('As senhas não coincidem')

            if User.objects.filter(username=nome_usuario).exists():
                return render_error('Já existe um usuário com este nome.')
            
            if User.objects.filter(email=email_usuario).exists():
                return render_error('Este e-mail já está cadastrado.')
            
            user_type = request.POST.get('user_type')
            if not user_type in ['client', 'professional']:
                return render_error('Por favor, selecione se você é um Cliente ou Profissional.')

            meu_user = User.objects.create_user(
                username=nome_usuario,
                email=email_usuario,
                password=senha
            )
            
            Profile.objects.create(user=meu_user, user_type=user_type)
            
            messages.success(request, 'Usuário criado com sucesso! Faça o login.')
            return redirect('login') 

    else:
        # GARANTE QUE O FORMULÁRIO ESTEJA SEMPRE LIMPO EM UM NOVO ACESSO
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def recover_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            messages.success(request, 'Se o e-mail estiver cadastrado, você receberá instruções para redefinir a senha.')
        else:
            messages.error(request, 'Informe um e-mail válido.')
    return render(request, 'accounts/recover_password.html')

# Views de exemplo para os dashboards
def dashboard_cliente(request):
    # CORRIGIDO: O caminho do template deve incluir o subdiretório do app
    return render(request, 'projects/cliente/dashboard.html')

def dashboard_profissional(request):
    # CORRIGIDO: O caminho do template deve incluir o subdiretório do app
    return render(request, 'projects/profissional/dashboardP.html')

def inicio(request):
    # CORRIGIDO: Redireciona para a página de login, já que 'index.html' não existe.
    return redirect('login')

def logout(request):
    auth_logout(request)
    return redirect('inicio')

