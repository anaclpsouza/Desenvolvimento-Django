from django.shortcuts import render, redirect, get_object_or_404
from .models import Instrutor, PerfilInstrutor, Area


def principal(request):
    return render(request, 'curso/principal.html')


def lista_instrutor(request):
    ordenacao = request.GET.get('ordenar', '')
    campos_validos = ['nome', 'idade', 'especialidade']

    if ordenacao in campos_validos:
        instrutores = Instrutor.objects.select_related('perfil').order_by(ordenacao)
    else:
        instrutores = Instrutor.objects.select_related('perfil').order_by('id')

    contexto = {
        'instrutores': instrutores,
        'ordenacao': ordenacao,
    }
    return render(request, 'curso/lista_instrutor.html', contexto)


def cria_instrutor(request):
    if request.method == 'POST':
        instrutor = Instrutor.objects.create(
            nome=request.POST.get('nome'),
            idade=int(request.POST.get('idade')),
            email=request.POST.get('email'),
            especialidade=request.POST.get('especialidade'),
            codigo=request.POST.get('codigo'),
            curriculo=request.POST.get('curriculo') or None,
        )
        PerfilInstrutor.objects.create(
            instrutor=instrutor,
            biografia=request.POST.get('biografia'),
            linkedin=request.POST.get('linkedin') or None,
        )
        return redirect('curso:lista_instrutor')

    return render(request, 'curso/cria_instrutor.html')


def consulta_instrutor(request, id_instrutor):
    instrutor = get_object_or_404(Instrutor.objects.select_related('perfil'), id=id_instrutor)
    return render(request, 'curso/consulta_instrutor.html', {'instrutor': instrutor})


def atualiza_instrutor(request, id_instrutor):
    instrutor = get_object_or_404(Instrutor, id=id_instrutor)
    perfil, _ = PerfilInstrutor.objects.get_or_create(
        instrutor=instrutor,
        defaults={'biografia': ''},
    )

    if request.method == 'POST':
        instrutor.nome = request.POST.get('nome')
        instrutor.idade = int(request.POST.get('idade'))
        instrutor.email = request.POST.get('email')
        instrutor.especialidade = request.POST.get('especialidade')
        instrutor.curriculo = request.POST.get('curriculo') or None
        instrutor.ativo = request.POST.get('ativo') == 'on'
        instrutor.save()

        perfil.biografia = request.POST.get('biografia')
        perfil.linkedin = request.POST.get('linkedin') or None
        perfil.save()

        return redirect('curso:lista_instrutor')

    contexto = {
        'instrutor': instrutor,
        'perfil': perfil,
    }
    return render(request, 'curso/atualiza_instrutor.html', contexto)


def exclui_instrutor(request, id_instrutor):
    instrutor = get_object_or_404(Instrutor, id=id_instrutor)
    instrutor.delete()
    return redirect('curso:lista_instrutor')


def lista_instrutor_60(request):
    instrutores = Instrutor.objects.select_related('perfil').filter(idade__gte=60)
    return render(request, 'curso/lista_instrutor_60.html', {'instrutores': instrutores})


def lista_area(request):
    areas = Area.objects.all()
    return render(request, 'curso/lista_area.html', {'areas': areas})


def cria_area(request):
    if request.method == 'POST':
        Area.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao') or None,
            ativa=request.POST.get('ativa') == 'on',
        )
        return redirect('curso:lista_area')

    return render(request, 'curso/cria_area.html')


def consulta_area(request, id_area):
    area = get_object_or_404(Area, id=id_area)
    return render(request, 'curso/consulta_area.html', {'area': area})


def atualiza_area(request, id_area):
    area = get_object_or_404(Area, id=id_area)

    if request.method == 'POST':
        area.nome = request.POST.get('nome')
        area.descricao = request.POST.get('descricao') or None
        area.ativa = request.POST.get('ativa') == 'on'
        area.save()
        return redirect('curso:lista_area')

    return render(request, 'curso/atualiza_area.html', {'area': area})


def exclui_area(request, id_area):
    area = get_object_or_404(Area, id=id_area)
    area.delete()
    return redirect('curso:lista_area')


def pesquisa_area(request):
    termo = request.GET.get('nome', '')
    if termo:
        areas = Area.objects.filter(nome__contains=termo)
    else:
        areas = Area.objects.none()

    contexto = {
        'areas': areas,
        'termo': termo,
    }
    return render(request, 'curso/pesquisa_area.html', contexto)
