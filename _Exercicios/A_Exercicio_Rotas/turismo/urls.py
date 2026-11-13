from django.urls import path
from . import views

app_name = "turismo"

urlpatterns = [
    path('turismo/', views.turismo, name="home"),
    path('turismo/ponto/<str:nome>/', views.ponto, name="ponto"),
    path('turismo/redirecionar-prefeitura/', views.redirecionar, name="redirecionar_prefeitura"),
    path('turismo/pesquisa/', views.pesquisa, name="pesquisa")
]