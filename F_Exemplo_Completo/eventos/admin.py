from django.contrib import admin
from .models import Categoria, Organizador, PerfilOrganizador, Palestrante, Evento


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao', 'ativa']
    list_display_links = ['nome']
    list_editable = ['ativa']
    list_filter = ['ativa']
    ordering = ['ativa', 'nome']
    fields = [('id', 'nome'), 'descricao', 'ativa']
    readonly_fields = ['id']
    search_fields = ['nome']
    search_help_text = 'Digite o nome da categoria para pesquisar.'


@admin.register(Organizador)
class OrganizadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'nome', 'email', 'ativo']
    list_display_links = ['id', 'nome']
    list_editable = ['email']
    list_filter = ['ativo']
    ordering = ['nome']
    fields = [('id', 'codigo'), 'nome', 'email', 'telefone', 'ativo']
    readonly_fields = ['id']
    search_fields = ['nome', 'email', 'codigo']
    search_help_text = 'Digite o nome, email ou código para pesquisar.'


@admin.register(PerfilOrganizador)
class PerfilOrganizadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_organizador']
    list_display_links = ['id']
    ordering = ['organizador__nome']
    fields = ['id', 'organizador', 'biografia', 'linkedin']
    readonly_fields = ['id']
    search_fields = ['organizador__nome', 'biografia']
    search_help_text = 'Digite o nome do organizador ou biografia para pesquisar.'

    @admin.display(description='Organizador', ordering='organizador__nome')
    def nome_organizador(self, obj):
        return obj.organizador.nome


@admin.register(Palestrante)
class PalestranteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'especialidade', 'idade']
    list_display_links = ['id', 'nome']
    list_filter = ['especialidade']
    ordering = ['nome']
    fields = ['id', 'nome', 'especialidade', 'idade']
    readonly_fields = ['id']
    search_fields = ['nome', 'especialidade']
    search_help_text = 'Digite o nome ou especialidade para pesquisar.'


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_evento', 'nome_categoria', 'valor', 'vagas', 'ativo']
    list_display_links = ['id', 'titulo']
    list_editable = ['data_evento', 'ativo']
    list_filter = ['categoria', 'organizador', 'ativo']
    ordering = ['ativo', 'data_evento']
    fields = [
        'id',
        'titulo',
        'descricao',
        ('data_evento', 'ativo'),
        ('valor', 'vagas'),
        'categoria',
        'organizador',
        'palestrantes',
        'criado_em',
    ]
    raw_id_fields = ['palestrantes']
    readonly_fields = ['id', 'criado_em']
    search_fields = ['titulo', 'descricao', 'categoria__nome']
    search_help_text = 'Digite o título, descrição ou categoria para pesquisar.'

    @admin.display(description='Categoria', ordering='categoria__nome')
    def nome_categoria(self, obj):
        return obj.categoria.nome
