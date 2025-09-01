from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def inicio(request):
	return render(request, 'landingpage/inicio.html')

def dashboard(request):
	return render(request, 'projects/cliente/dashboard.html')

def profissionais(request):
	return render(request, 'projects/cliente/profissionais.html')

def mensagens(request):
	return render(request, 'projects/cliente/mensagens.html')

def pagamento(request):
	return render(request, 'projects/cliente/pagamento.html')

def avaliacao(request):
	return render(request, 'projects/cliente/avaliacao.html')

def perfil(request):
	return render(request, 'projects/cliente/perfil.html')

def meusprojetos(request):
	return render(request, 'projects/cliente/meusprojetos.html')

def inicioP(request):
	return render(request, 'projects/profissional/inicioP.html')

def clientesP(request):
    return render(request, 'projects/profissional/clientesP.html')

def dashboardP(request):
    return render(request, 'projects/profissional/dashboardP.html')

def mensagensP(request):
    return render(request, 'projects/profissional/mensagensP.html')

def meusprojetosP(request):
    return render(request, 'projects/profissional/meusprojetosP.html')

def pagamentoP(request):
    return render(request, 'projects/profissional/pagamentoP.html')

def perfilP(request):
    return render(request, 'projects/profissional/perfilP.html')

def procurarprojetosP(request):
    return render(request, 'projects/profissional/procurarprojetosP.html')
	
@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        return redirect('home')  # ou a página inicial
    return redirect('perfilP')

