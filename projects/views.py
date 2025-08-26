from django.shortcuts import render

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
	


