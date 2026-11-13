from django.urls import path
from . import views

app_name = "cidade"

urlpatterns = [
    path('cidade/', views.cidade, name="home"),
    path('cidade/bairro/<str:nome>/', views.bairro, name="bairro"),
    path('cidade/prefeitura/', views.prefeitura_padrao, name="prefeitura_padrao"),
    path('cidade/prefeitura/<str:prefeito>/', views.prefeitura, name="prefeitura")
]