from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'titulo': 'Inicio',
        'page': 'index'
    }
    return render(request, "cerva/index.html", context)

def contato(request):
    context = {
        'titulo': 'Contato',
        'page': 'contato'
    }
    return render(request, "cerva/contato.html", context)

def historia(request):
    context = {
        'titulo': 'Historia da Cerveja',
        'page': 'Historia'
    }
    return render(request, "cerva/01-historia.html", context)

def escolas(request):
    context = {
        'titulo': 'Escolas Cervejeiras',
        'page': 'escolas'
    }
    return render(request, "cerva/02-escolas.html", context)

def alema(request):
    context = {
        'titulo': 'Escola Alemã',
        'page': 'alema'
    }
    return render(request, "cerva/03-alema.html", context)

def inglesa(request):
    context = {
        'titulo': 'Escola Inglesa',
        'page': 'inglesa'
    }
    return render(request, "cerva/04-inglesa.html", context)

def belga(request):
    context = {
        'titulo': 'Escola Belga',
        'page': 'belga'
    }
    return render(request, "cerva/05-belga.html", context)

def americana(request):
    context = {
        'titulo': 'Escola Americana',
        'page': 'americana'
    }
    return render(request, "cerva/06-americana.html", context)

def pureza(request):
    context = {
        'titulo': 'Lei de Pureza Alemã',
        'page': 'pureza'
    }
    return render(request, "cerva/07-pureza.html", context)

def cerveja(request):
    context = {
        'titulo': 'O que é Cerveja?',
        'page': 'cerveja'
    }
    return render(request, "cerva/08-cerveja.html", context)

def harmonizacao(request):
    context = {
        'titulo': 'Harmonização de Cervejas',
        'page': 'harmonizacao'
    }
    return render(request, "cerva/09-harmonizacao.html", context)

def fabricacao(request):
    context = {
        'titulo': 'Como Fazer Cerveja?',
        'page': 'fabricacao'
    }
    return render(request, "cerva/10-fabricacao.html", context)