from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>Área de Home</h1>')

def produtos(request):
    return HttpResponse('<h1>Área de produtos</h1>')

def clientes(request):
    return HttpResponse('<h1>Área de Clientes</h1>')

    
 