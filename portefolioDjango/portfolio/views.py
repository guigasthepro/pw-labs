from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_page_view(request):
	return render(request, 'home.html')

def contacto_page_view(request):
	return render(request, 'contacto.html')

def projetoscurso_page_view(request):
	return render(request, 'projetoscurso.html')

def projetospessoais_page_view(request):
	return render(request, 'projetospessoais.html')

def projetosescola_page_view(request):
	return render(request, 'projetosescola.html')

def sobre_page_view(request):
	return render(request, 'sobre.html')