from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .service import validar_dados

# Create your views here.

@csrf_exempt
def cadastro(request):
    if request.method == 'GET':
        html = """
            <html lang="pt-br">
            <head> 
                <meta charset="UTF-8">
                <title> Formulário HTML </title>
            </head>
            <body>
                <h1> Formulário </h1>
                <form action='' method='POST'>
                    <label for="nome">Nome: </label>
                    <input type="text" id="nome" name="nome">
                    <label for="email">Email: </label>
                    <input type="text" id="email" name="email">
                    <button type="submit"> Enviar </button>
                </form>
                </body>
            </html>
        """

        return HttpResponse(html)
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        valido, mensagem = validar_dados(nome, email)
        if valido:
            return HttpResponse(f"Cadastro realizado com sucesso! Nome: {nome}, Email: {email}")
        else:
            return HttpResponse(f"Erro: {mensagem}")
    return HttpResponse("Método não permitido")

def perfil(request, usuario):
    dados = {
        "nome": f"{usuario}",
        "idade": 20,
        "email": f"{usuario}@email.com",
        "instagram": f"@{usuario}"
    }
    return JsonResponse(dados)

def rota(request):
    rota_completa = request.get_full_path()
    return HttpResponse(f"A Rota completa é: {rota_completa}")