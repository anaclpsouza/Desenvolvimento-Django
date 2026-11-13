from django.http import HttpResponse


def cidade(request):
    return HttpResponse("Bem-vindo à Cidade!")


def bairro(request, nome):
    return HttpResponse(f"Você está no bairro: {nome}")


def prefeitura_padrao(request, prefeito="Maria Silva"):
    return HttpResponse(f"O prefeito é: {prefeito}")


def prefeitura(request, prefeito):
    return HttpResponse(f"O prefeito é: {prefeito}")
