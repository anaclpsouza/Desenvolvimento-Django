from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    contexto = {
        "titulo_pagina": "Página inicial",
        "nome_usuario": "ana",
        "nome_curso": "bsi"
    }

    return render(request, 'institucional/index.html', contexto)

def info_campus(request):
    campus = {
        "nome": "campus manhuaçu",
        "cidade": "manhuaçu",
        "estado": "mg",
        "diretor": None,
        "ano_fundacao": "2000",
        "orcamento_anual": 1250000.758,
    }

    contexto = {
        "campus": campus
    }

    return render(request, 'institucional/campus.html', contexto)

def perfil_aluno(request):
    aluno = {
        "nome": "ana clara",
        "matricula": "20289392",
        "curso": {
            "nome": "bsi",
            "codigo": "292"
        },
        "notas": [8.56, 7.234, 9.876],
        "contato": {
            "email": "ana@email",
            "cidade": "mçu"
        }
    }

    contexto = {
        "aluno": aluno
    }

    return render(request, 'institucional/aluno.html', contexto)

def lista_cursos(request):
    cursos = [
        {
            "nome": "bacharelado em sistemas de informação",
            "carga_horaria": 3200.5,
            "vagas": 40,
            "ativo": True,
            "status": "Em Andamento",
            "ementa": "Estudo completo de desenvolvimento de software, bancos de dados, redes e engenharia."
        },
        {
            "nome": "técnico em informática",
            "carga_horaria": 1200.0,
            "vagas": 0,
            "ativo": True,
            "status": "Aguardando",
            "ementa": "Fundamentos de programação, manutenção de computadores, sistemas operacionais e web."
        },
        {
            "nome": "pós-graduação em desenvolvimento web",
            "carga_horaria": 360.75,
            "vagas": 1,
            "ativo": False,
            "status": "Suspenso Temporariamente",
            "ementa": "Arquitetura moderna de aplicações web com frameworks Python, APIs REST e nuvem."
        },
    ]

    codigo_simulado = None
    if request.method == "POST":
        codigo_simulado = request.POST.get("codigo")

    contexto = {
        "cursos": cursos,
        "total_cursos": len(cursos),
        "codigo_simulado": codigo_simulado,
    }

    return render(request, 'institucional/cursos.html', contexto)