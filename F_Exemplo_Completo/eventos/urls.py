from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.principal, name='principal'),
    path('sobre/', views.sobre_padrao, {'cidade': 'Manhuaçu'}, name='sobre_padrao'),
    path('sobre/<str:cidade>/', views.sobre, name='sobre'),
    path('ir-eventos/', views.redirecionar_eventos, name='redirecionar_eventos'),

    # Eventos CRUD + pesquisa + ordenação
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/criar/', views.cria_evento, name='cria_evento'),
    path('eventos/<int:id_evento>/', views.consulta_evento, name='consulta_evento'),
    path('eventos/<int:id_evento>/atualizar/', views.atualiza_evento, name='atualiza_evento'),
    path('eventos/<int:id_evento>/excluir/', views.exclui_evento, name='exclui_evento'),

    # Organizadores CRUD (com PerfilOrganizador OneToOne)
    path('organizadores/', views.lista_organizadores, name='lista_organizadores'),
    path('organizadores/criar/', views.cria_organizador, name='cria_organizador'),
    path('organizadores/<int:id_org>/', views.consulta_organizador, name='consulta_organizador'),
    path('organizadores/<int:id_org>/atualizar/', views.atualiza_organizador, name='atualiza_organizador'),
    path('organizadores/<int:id_org>/excluir/', views.exclui_organizador, name='exclui_organizador'),

    # Categorias
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/criar/', views.cria_categoria, name='cria_categoria'),

    # API JSON e rota atual (conceitos de Views)
    path('api/info/', views.api_info, name='api_info'),
    path('api/eventos/', views.api_eventos, name='api_eventos'),
    path('rota-atual/', views.rota_atual, name='rota_atual'),
]
