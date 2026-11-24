from django.contrib import admin
from .models import Instrutor, PerfilInstrutor, Area, Curso


@admin.register(Instrutor)
class InstrutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'especialidade']
    list_display_links = ['id', 'nome']
    list_editable = ['email']
    list_filter = ['especialidade', 'ativo']
    ordering = ['especialidade']
    fields = [('id', 'codigo'), 'nome', 'idade', 'email', 'especialidade', 'curriculo', 'ativo']
    readonly_fields = ['id']
    search_fields = ['nome', 'email', 'especialidade']
    search_help_text = 'Digite o nome, email ou especialidade para pesquisar.'


@admin.register(PerfilInstrutor)
class PerfilInstrutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_instrutor']
    list_display_links = ['id']
    ordering = ['instrutor__nome']
    fields = ['id', 'instrutor', 'biografia', 'linkedin']
    readonly_fields = ['id']
    search_fields = ['instrutor__nome', 'biografia']
    search_help_text = 'Digite o nome do instrutor ou biografia para pesquisar.'

    @admin.display(description='Instrutor', ordering='instrutor__nome')
    def nome_instrutor(self, obj):
        return obj.instrutor.nome


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao', 'ativa']
    list_display_links = ['nome']
    list_editable = ['ativa']
    list_filter = ['ativa']
    ordering = ['ativa', 'nome']
    fields = [('id', 'nome'), 'descricao', 'ativa']
    readonly_fields = ['id']
    search_fields = ['nome']
    search_help_text = 'Digite o nome da área para pesquisar.'


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_inicio', 'nome_area']
    list_display_links = ['id', 'titulo']
    list_editable = ['data_inicio']
    list_filter = ['instrutores', 'area', 'ativo']
    ordering = ['ativo', 'area__nome']
    fields = ['id', 'titulo', 'descricao', ('data_inicio', 'ativo'), 'instrutores', 'area']
    raw_id_fields = ['instrutores']
    readonly_fields = ['id']
    search_fields = ['titulo', 'descricao', 'area__nome']
    search_help_text = 'Digite o título, descrição ou nome da área para pesquisar.'

    @admin.display(description='Área', ordering='area__nome')
    def nome_area(self, obj):
        return obj.area.nome
