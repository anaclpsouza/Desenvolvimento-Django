from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('usuarios/cadastro/', views.cadastro, name="cadastro_usuario"),
    path('usuarios/perfil/<str:usuario>/', views.perfil, name="perfil_usuario"),
    path('usuarios/rota-atual/', views.rota, name="mostrar_rota")
]