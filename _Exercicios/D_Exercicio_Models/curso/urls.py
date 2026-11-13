from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.principal, name='principal'),
    path('instrutores/', views.lista_instrutor, name='lista_instrutor'),
    path('instrutores/criar/', views.cria_instrutor, name='cria_instrutor'),
    path('instrutores/maiores-60/', views.lista_instrutor_60, name='lista_instrutor_60'),
    path('instrutores/<int:id_instrutor>/', views.consulta_instrutor, name='consulta_instrutor'),
    path('instrutores/<int:id_instrutor>/atualizar/', views.atualiza_instrutor, name='atualiza_instrutor'),
    path('instrutores/<int:id_instrutor>/excluir/', views.exclui_instrutor, name='exclui_instrutor'),
    path('areas/', views.lista_area, name='lista_area'),
    path('areas/criar/', views.cria_area, name='cria_area'),
    path('areas/pesquisar/', views.pesquisa_area, name='pesquisa_area'),
    path('areas/<int:id_area>/', views.consulta_area, name='consulta_area'),
    path('areas/<int:id_area>/atualizar/', views.atualiza_area, name='atualiza_area'),
    path('areas/<int:id_area>/excluir/', views.exclui_area, name='exclui_area'),
]
