from django.urls import path
from . import views

app_name = "operacoes"

urlpatterns = [
    path('soma/', views.soma, name="soma"),
    path('subtracao/<int:n1>/<int:n2>/', views.subtracao),
    path('divisao/<int:n1>/<int:n2>/', views.divisao),
    path('multiplicacao/<int:n1>/<int:n2>/', views.multiplicacao)
]