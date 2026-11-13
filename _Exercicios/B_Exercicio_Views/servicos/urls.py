from django.urls import path
from . import views

app_name = "servicos"

urlpatterns = [
    path('servicos/calcular-desconto/', views.calcular_desconto, name="calcular_desconto"),
    path('servicos/mensagem/<str:usuario>/', views.mensagem, name="mensagem_usuario"),
    path('servicos/maior/', views.maior, name="maior"),
    path('servicos/api-info/', views.api, name="api_info")
]