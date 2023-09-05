from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg

# serializers serve para transformar e destransformar obj JSON

# serializer do model avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    # curso = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name="curso-detail"
    # )

    # configuracao do serializer
    class Meta:
        # informando de qual model se trata
        model = Avaliacao

        # campos que irao ser mostrados ao consultar este model
        fields = (
            'id',
            'nome',
            'avaliacao',
            'comentario',
            # ao consultar este model, nao e legal mostrar o campo email (privacidade)
            'email',
            'criacao',
            'ativo',
            'curso'
        )

        # apenas permitido escrever o email (cadastro) na hora da consulta ele nao ira retornar
        extra_kwargs = {
            'email': {'write_only': True}
        }

    # validando um dado da tabela
    # sempre este padrao (validade_nomeDoCampo)
    def validate_avaliacao(self, valor):
        if (valor > 0) and (valor <= 5):
            return valor
        raise serializers.ValidationError(
            "A avaliação deve ser entre 1 e 5")


# serializer de curso


class CursoSerializer(serializers.ModelSerializer):
    # # nested relationship (retornar as avaliacoes dos cursos)

    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #  Hyper linked Related Field retorna o LINK das avaliacoes dos cursos (recomendado API-REST)

    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="avaliacao-detail"
    # )

    # Primary Key Related Field (retorna a pk das avaliacoes)

    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # este campo recebe uma funcao e retorna o valor de forma dinamica
    # sempre este padrao (def: get_nomeDaVariavel)
    media_avaliacoes = serializers.SerializerMethodField()

    def get_media_avaliacoes(self, obj):
        # avaliacoes é o nome da chave estrangeira do model (models.py)
        media = obj.avaliacoes.aggregate(
            Avg('avaliacao')).get("avaliacao__avg")

        if media is None:
            return 0
        return round(media, ndigits=2)

    class Meta:
        model = Curso

        # tds os campos podem ser mostrados
        fields = '__all__'
