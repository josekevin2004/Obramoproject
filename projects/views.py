from django.shortcuts import render

def inicio(request):
	return render(request, 'landingpage/inicio.html')

def dashboard(request):
	return render(request, 'projects/dashboard.html')

def profissionais(request):
	return render(request, 'projects/profissionais.html')

def mensagens(request):
	return render(request, 'projects/mensagens.html')

def pagamento(request):
	return render(request, 'projects/pagamento.html')

def avaliacao(request):
	return render(request, 'projects/avaliacao.html')

def perfil(request):
	return render(request, 'projects/perfil.html')

def meusprojetos(request):
	return render(request, 'projects/meusprojetos.html')
	


