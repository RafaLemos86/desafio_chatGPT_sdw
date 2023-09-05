from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerializer


class AvaliacaoAPIView(APIView):

    """
    api da avaliacao dos cursos
    """

    def get(self, request):
        # pegando todas as avaliacoes
        avaliacoes = Avaliacao.objects.all()
        # parametro many pois sao mais de um registro
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        # serializando os dados recebidos
        serializer = AvaliacaoSerializer(data=request.data)
        # se os dados forem invalidos, msg de erro
        serializer.is_valid(raise_exception=True)
        # salvando no BD
        serializer.save()
        # retorna
        return Response({"msg": "A avaliação foi registrada com sucesso"}, status=status.HTTP_201_CREATED)


class CursoAPIView(APIView):

    """
    API dos cursos
    """

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # serializando os dados recebidos
        serializer = CursoSerializer(data=request.data)
        # se os dados forem invalidos, msg de erro
        serializer.is_valid(raise_exception=True)
        # salvando no BD
        serializer.save()
        # retorna
        return Response(serializer.data, status=status.HTTP_201_CREATED)
