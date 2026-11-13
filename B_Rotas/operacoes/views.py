from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def soma(request):
    n1 = request.GET.get("n1")
    n2 = request.GET.get("n2")
    resultado = int(n1) + int(n2)
    return HttpResponse(f"A soma entre {n1} e {n2} é {resultado}")

def subtracao(request, n1, n2):
    return HttpResponse(f"A subtração entre {n1} e {n2} é {n1 - n2}")

def multiplicacao(request, n1, n2):
    return HttpResponse(f"A multiplicação entre {n1} e {n2} é {n1 * n2}")

def divisao(request, n1, n2):
    return HttpResponse(f"A divisão entre {n1} e {n2} é {n1 / n2}")

