from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        db_table = 'eventos_categoria'
        ordering = ['nome']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome


class Organizador(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'eventos_organizador'
        ordering = ['nome']
        verbose_name = 'Organizador'
        verbose_name_plural = 'Organizadores'

    def __str__(self):
        return self.nome


class PerfilOrganizador(models.Model):
    organizador = models.OneToOneField(Organizador, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.TextField()
    linkedin = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'eventos_perfil_organizador'
        ordering = ['organizador']
        verbose_name = 'Perfil do Organizador'
        verbose_name_plural = 'Perfis dos Organizadores'

    def __str__(self):
        return f"Perfil de {self.organizador.nome}"


class Palestrante(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()

    class Meta:
        db_table = 'eventos_palestrante'
        ordering = ['nome']
        verbose_name = 'Palestrante'
        verbose_name_plural = 'Palestrantes'

    def __str__(self):
        return f"{self.nome} ({self.especialidade})"


class Evento(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    data_evento = models.DateField()
    valor = models.FloatField(default=0.0)
    vagas = models.PositiveIntegerField(default=30)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)
    palestrantes = models.ManyToManyField(Palestrante, blank=True)

    class Meta:
        db_table = 'eventos_evento'
        ordering = ['data_evento', 'titulo']
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.titulo
