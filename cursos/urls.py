from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (CursoAPIView,
                    AvaliacaoAPIView,
                    AvaliacoesAPIView,
                    CursosAPIView,
                    AvaliacaoViewSet,
                    CursoViewSet)


# V2 da API (ViewSet e Router)
router = SimpleRouter()
router.register("cursos", CursoViewSet)
router.register("avaliacoes", AvaliacaoViewSet)

# V1 da API (generics)
urlpatterns = [
    # retorna todos os cursos
    path("cursos/", CursosAPIView.as_view(), name='cursos'),

    # retorna um curso pelo id
    path("cursos/<int:pk>", CursoAPIView.as_view(), name="curso"),

    # retorna todas as avaliacoes de um curso(id)
    path("cursos/<int:curso_pk>/avaliacoes/",
         AvaliacoesAPIView.as_view(), name="curso_avaliacoes"),

    # retora uma avaliacao(id) para um curso(id)
    path("cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/",
         AvaliacaoAPIView.as_view(), name="curso_avaliacao"),

    # retorna todas as avaliacoes
    path("avaliacoes/", AvaliacoesAPIView.as_view(), name="avaliacoes"),

    # retorna uma avaliacao pelo id
    path("avaliacoes/<int:avaliacao_pk>/",
         AvaliacaoAPIView.as_view(), name="avaliacao"),
]
