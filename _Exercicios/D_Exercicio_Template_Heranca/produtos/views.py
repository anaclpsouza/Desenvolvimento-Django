from django.shortcuts import render, redirect

PRODUTOS = [
    {
        "id": 1,
        "nome": "notebook gamer pro",
        "preco": 5499.90,
        "resumo": "Notebook de alto desempenho com placa de vídeo dedicada para jogos e trabalho pesado.",
        "descricao": "Equipado com processador de última geração, 16GB de RAM DDR5, SSD NVMe de 1TB e tela de 144Hz para máxima fluidez.",
        "promocao": True,
    },
    {
        "id": 2,
        "nome": "mouse sem fio ergonômico",
        "preco": 189.50,
        "resumo": "Mouse óptico sem fio com design ergonômico e bateria recarregável de longa duração.",
        "descricao": "Conexão Bluetooth e receptor USB 2.4GHz com ajuste de DPI até 4000, ideal para uso prolongado no escritório ou em casa.",
    },
    {
        "id": 3,
        "nome": "teclado mecânico rgb",
        "preco": 349.99,
        "resumo": "Teclado mecânico compacto com switches táteis e iluminação RGB personalizável.",
        "descricao": "Construção em alumínio reforçado, teclas double-shot resistentes ao desgaste e cabo USB-C removível para fácil transporte.",
        "promocao": True,
    },
    {
        "id": 4,
        "nome": "monitor ultrawide 29 polegadas",
        "preco": 1299.00,
        "resumo": "Monitor IPS ultrawide ideal para produtividade com múltiplas janelas lado a lado.",
        "descricao": "Resolução Full HD 2560x1080, fidelidade de cores sRGB 99%, entradas HDMI e DisplayPort com suporte a ajuste de inclinação.",
    },
    {
        "id": 5,
        "nome": "headset bluetooth com cancelamento",
        "preco": 459.75,
        "resumo": "Fone de ouvido sem fio com cancelamento ativo de ruído e microfone integrado.",
        "descricao": "Almofadas confortáveis em espuma viscoelástica, autonomia de até 30 horas de reprodução contínua e carregamento rápido via USB-C.",
    },
]


def index(request):
    contexto = {
        "produtos": PRODUTOS,
        "total_produtos": len(PRODUTOS),
    }
    return render(request, 'produtos/lista_produtos.html', contexto)


def produto(request, id):
    if request.method == 'POST':
        return redirect('produtos:index')

    item = next((p for p in PRODUTOS if p['id'] == id), None)
    contexto = {
        "produto": item,
    }
    return render(request, 'produtos/detalhe_produto.html', contexto)
