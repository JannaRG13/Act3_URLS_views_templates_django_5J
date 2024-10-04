from django.shortcuts import render
from django.http import HttpResponse

# CREATE VIEWS
def index(request): 
    return render(request, 'index.html')

def agencia(request): 
    return render(request, 'agencia.html')

def cliente(request): 
    return render(request, 'cliente.html')

def empleado(request): 
    return render(request, 'empleado.html')

def vehiculo(request): 
    return render(request, 'vehiculo.html')