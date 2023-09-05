from django.db import models

# Create your models here.


class Base(models.Model):
    # atributos do model curso
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    # url unica para cada curso
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['id']

    # print
    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    # chave estrangeira para curso

    # PARA, DELECAO, PERMITIR BUSCAS CUSTOMIZADAS
    curso = models.ForeignKey(
        Curso, on_delete=models.CASCADE, related_name="avaliacoes")
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    # de 0 a 10 com 1 decimal
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        # um email e um curso sao combinacoes unicas
        unique_together = ['email', 'curso']
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com a nota {self.avaliacao}'
