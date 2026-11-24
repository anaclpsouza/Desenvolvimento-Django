from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import Categoria, Organizador, PerfilOrganizador, Palestrante, Evento


def principal(request):
    contexto = {
        'total_eventos': Evento.objects.count(),
        'total_organizadores': Organizador.objects.count(),
        'total_categorias': Categoria.objects.count(),
        'proximos_eventos': Evento.objects.filter(ativo=True).select_related('categoria', 'organizador')[:3],
    }
    return render(request, 'eventos/principal.html', contexto)


def sobre_padrao(request, cidade='Manhuaçu'):
    return HttpResponse(f"Sistema de Eventos Acadêmicos - Campus {cidade}")


def sobre(request, cidade):
    return HttpResponse(f"Sistema de Eventos Acadêmicos - Campus {cidade}")


def redirecionar_eventos(request):
    return redirect('eventos:lista_eventos')


def lista_eventos(request):
    termo = request.GET.get('q', '')
    ordenacao = request.GET.get('ordenar', '')
    categoria_id = request.GET.get('categoria', '')

    eventos = Evento.objects.select_related('categoria', 'organizador').prefetch_related('palestrantes')

    if termo:
        eventos = eventos.filter(titulo__contains=termo)

    if categoria_id:
        eventos = eventos.filter(categoria_id=categoria_id)

    campos_validos = ['titulo', 'data_evento', 'valor', 'vagas']
    if ordenacao in campos_validos:
        eventos = eventos.order_by(ordenacao)

    contexto = {
        'eventos': eventos,
        'categorias': Categoria.objects.filter(ativa=True),
        'termo': termo,
        'ordenacao': ordenacao,
        'categoria_id': categoria_id,
        'total': eventos.count(),
    }
    return render(request, 'eventos/lista_eventos.html', contexto)


def cria_evento(request):
    if request.method == 'POST':
        evento = Evento.objects.create(
            titulo=request.POST.get('titulo'),
            descricao=request.POST.get('descricao'),
            data_evento=request.POST.get('data_evento'),
            valor=float(request.POST.get('valor') or 0),
            vagas=int(request.POST.get('vagas') or 0),
            ativo=request.POST.get('ativo') == 'on',
            categoria_id=int(request.POST.get('categoria')),
            organizador_id=int(request.POST.get('organizador')),
        )
        palestrantes_ids = request.POST.getlist('palestrantes')
        if palestrantes_ids:
            evento.palestrantes.set(palestrantes_ids)
        return redirect('eventos:lista_eventos')

    contexto = {
        'categorias': Categoria.objects.filter(ativa=True),
        'organizadores': Organizador.objects.filter(ativo=True),
        'palestrantes': Palestrante.objects.all(),
    }
    return render(request, 'eventos/cria_evento.html', contexto)


def consulta_evento(request, id_evento):
    evento = get_object_or_404(
        Evento.objects.select_related('categoria', 'organizador').prefetch_related('palestrantes'),
        id=id_evento,
    )
    if request.method == 'POST':
        if evento.vagas > 0:
            evento.vagas -= 1
            evento.save()
        return redirect('eventos:consulta_evento', id_evento=evento.id)

    return render(request, 'eventos/consulta_evento.html', {'evento': evento})


def atualiza_evento(request, id_evento):
    evento = get_object_or_404(Evento, id=id_evento)

    if request.method == 'POST':
        evento.titulo = request.POST.get('titulo')
        evento.descricao = request.POST.get('descricao')
        evento.data_evento = request.POST.get('data_evento')
        evento.valor = float(request.POST.get('valor') or 0)
        evento.vagas = int(request.POST.get('vagas') or 0)
        evento.ativo = request.POST.get('ativo') == 'on'
        evento.categoria_id = int(request.POST.get('categoria'))
        evento.organizador_id = int(request.POST.get('organizador'))
        evento.save()

        palestrantes_ids = request.POST.getlist('palestrantes')
        evento.palestrantes.set(palestrantes_ids)
        return redirect('eventos:lista_eventos')

    contexto = {
        'evento': evento,
        'categorias': Categoria.objects.all(),
        'organizadores': Organizador.objects.all(),
        'palestrantes': Palestrante.objects.all(),
        'palestrantes_selecionados': list(evento.palestrantes.values_list('id', flat=True)),
    }
    return render(request, 'eventos/atualiza_evento.html', contexto)


def exclui_evento(request, id_evento):
    evento = get_object_or_404(Evento, id=id_evento)
    evento.delete()
    return redirect('eventos:lista_eventos')


def lista_organizadores(request):
    organizadores = Organizador.objects.select_related('perfil').all()
    return render(request, 'eventos/lista_organizadores.html', {'organizadores': organizadores})


def cria_organizador(request):
    if request.method == 'POST':
        org = Organizador.objects.create(
            codigo=request.POST.get('codigo'),
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone') or None,
        )
        PerfilOrganizador.objects.create(
            organizador=org,
            biografia=request.POST.get('biografia'),
            linkedin=request.POST.get('linkedin') or None,
        )
        return redirect('eventos:lista_organizadores')

    return render(request, 'eventos/cria_organizador.html')


def consulta_organizador(request, id_org):
    organizador = get_object_or_404(Organizador.objects.select_related('perfil'), id=id_org)
    return render(request, 'eventos/consulta_organizador.html', {'organizador': organizador})


def atualiza_organizador(request, id_org):
    organizador = get_object_or_404(Organizador, id=id_org)
    perfil, _ = PerfilOrganizador.objects.get_or_create(
        organizador=organizador,
        defaults={'biografia': ''},
    )

    if request.method == 'POST':
        organizador.nome = request.POST.get('nome')
        organizador.email = request.POST.get('email')
        organizador.telefone = request.POST.get('telefone') or None
        organizador.ativo = request.POST.get('ativo') == 'on'
        organizador.save()

        perfil.biografia = request.POST.get('biografia')
        perfil.linkedin = request.POST.get('linkedin') or None
        perfil.save()
        return redirect('eventos:lista_organizadores')

    contexto = {
        'organizador': organizador,
        'perfil': perfil,
    }
    return render(request, 'eventos/atualiza_organizador.html', contexto)


def exclui_organizador(request, id_org):
    organizador = get_object_or_404(Organizador, id=id_org)
    organizador.delete()
    return redirect('eventos:lista_organizadores')


def lista_categorias(request):
    termo = request.GET.get('nome', '')
    if termo:
        categorias = Categoria.objects.filter(nome__contains=termo)
    else:
        categorias = Categoria.objects.all()

    return render(request, 'eventos/lista_categorias.html', {'categorias': categorias, 'termo': termo})


def cria_categoria(request):
    if request.method == 'POST':
        Categoria.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao') or None,
            ativa=request.POST.get('ativa') == 'on',
        )
        return redirect('eventos:lista_categorias')

    return render(request, 'eventos/cria_categoria.html')


def api_info(request):
    dados = {
        'sistema': 'Eventos Acadêmicos',
        'links': {
            'principal': reverse('eventos:principal'),
            'eventos': reverse('eventos:lista_eventos'),
            'organizadores': reverse('eventos:lista_organizadores'),
            'categorias': reverse('eventos:lista_categorias'),
            'api_eventos': reverse('eventos:api_eventos'),
            'rota_atual': reverse('eventos:rota_atual'),
        },
    }
    return JsonResponse(dados)


def api_eventos(request):
    lista = []
    for e in Evento.objects.select_related('categoria', 'organizador').all():
        lista.append({
            'id': e.id,
            'titulo': e.titulo,
            'data_evento': str(e.data_evento),
            'valor': e.valor,
            'vagas': e.vagas,
            'categoria': e.categoria.nome,
            'organizador': e.organizador.nome,
            'ativo': e.ativo,
        })
    return JsonResponse({'eventos': lista})


def rota_atual(request):
    return HttpResponse(f"Rota completa acessada: {request.get_full_path()}")
