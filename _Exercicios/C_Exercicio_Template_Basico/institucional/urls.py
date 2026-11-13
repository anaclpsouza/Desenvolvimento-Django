from django.urls import path
from . import views

app_name = "institucional"

urlpatterns = [
    path('institucional/', views.index, name="index"),
    path('institucional/campus/', views.info_campus, name="info_campus"),
    path('institucional/aluno/', views.perfil_aluno, name="perfil_aluno"),
    path('institucional/cursos/', views.lista_cursos, name="lista_cursos"),
]