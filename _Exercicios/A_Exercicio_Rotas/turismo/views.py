from django.shortcuts import render, redirect 
from django.http import HttpResponse

# Create your views here.

def turismo(request):
    return HttpResponse("Bem-vindo ao Turismo!")

def ponto(request, nome):
    return HttpResponse(f"Você está visitando o ponto turístico: {nome}")

def redirecionar(request):
    return redirect("cidade:prefeitura_padrao")

def pesquisa(request):
    setor = request.GET.get("setor", "")
    guia = request.GET.get("guia", "").lower()
    if guia == "sim":
        texto_guia = "com guia"
    else:
        texto_guia = "sem guia"
    return HttpResponse(
        f"Seguem os resultados para possibilidade de turismo no setor '{setor}' {texto_guia}."
    )