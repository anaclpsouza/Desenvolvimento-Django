from django.db import models


class Instrutor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    especialidade = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    codigo = models.CharField(max_length=10, unique=True)
    curriculo = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'curso_instrutor'
        ordering = ['nome']
        verbose_name = 'Instrutor'
        verbose_name_plural = 'Instrutores'

    def __str__(self):
        return self.nome


class PerfilInstrutor(models.Model):
    instrutor = models.OneToOneField(Instrutor, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.TextField()
    linkedin = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'curso_perfil_instrutor'
        ordering = ['instrutor']
        verbose_name = 'Perfil do Instrutor'
        verbose_name_plural = 'Perfis dos Instrutores'

    def __str__(self):
        return f"Perfil de {self.instrutor.nome}"


class Area(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        db_table = 'curso_area'
        ordering = ['nome']
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

    def __str__(self):
        return self.nome


class Curso(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    data_inicio = models.DateField()
    instrutores = models.ManyToManyField(Instrutor)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'curso_curso'
        ordering = ['titulo']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo
