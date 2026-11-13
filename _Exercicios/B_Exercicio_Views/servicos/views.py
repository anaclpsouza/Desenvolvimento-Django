from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

def calcular_desconto(request):
    preco_str = request.GET.get("preco", "0")
    desconto_str = request.GET.get("desconto", "0")
    preco = float(preco_str)
    desconto = float(desconto_str)

    percentual = desconto / 100
    valor_descontado = preco * percentual
    valor_final = preco - valor_descontado
    return HttpResponse(f"Preço com desconto: R$ {valor_final:.2f}")

def mensagem(request, usuario):
    if usuario == "Paulo":
        return HttpResponse("Paulo, você precisa realizar a troca da sua senha.")
    elif usuario == "Pedro":
        return HttpResponse("Pedro, você precisa confirmar o seu email.")
    else:
        return HttpResponse("Não há mensagens pendentes.")

def maior(request):
    n1 = request.GET.get("n1")
    n2 = request.GET.get("n2")
    n3 = request.GET.get("n3")
    if n1 is None or n2 is None or n3 is None:
        return HttpResponse("Informe os parâmetros n1, n2 e n3.")
    maior = max(int(n1), int(n2), int(n3))
    return HttpResponse(f"<h1>O maior número é: {maior}</h1>")

def api(request):
    dados = {
        "links": {
            'maior': reverse("servicos:maior") + '?n1=100&n2=5&n3=3',
            'calcular_desconto': reverse("servicos:calcular_desconto") + '?preco=100&desconto=5',
            'mensagem_usuario': reverse("servicos:mensagem_usuario", kwargs={"usuario": "pedro"}),
            'api-info': reverse('servicos:api_info')
        }
    }

    return JsonResponse(dados)
    