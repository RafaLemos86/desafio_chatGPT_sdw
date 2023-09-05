import requests
import openai
from random import randint

openai.api_key = "SEU TOKEN"
TOKEN_API_CURSO = "token 46a48747c49fa70c69c33a7bdf886f0fdd6fe1f0"
URL_BASE = 'http://localhost:8000/api/v2/'


class CriarAvaliacao:
    def __init__(self, id_curso):
        self.headers = {"Authorization": TOKEN_API_CURSO}
        self.id_curso = id_curso
        self.url = f'{URL_BASE}cursos/{self.id_curso}/'
        self.url2 = f'{URL_BASE}avaliacoes/'

    def _obter_informacoes_curso(self):
        result = requests.get(url=self.url, headers=self.headers)
        if result.status_code == 200:
            data = result.json()
            return data
        else:
            raise ValueError("O ID do curso informado não existe")

    def _gerar_texto_aleatorio(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip('\"')

    def gerar_avaliacao(self):
        informacoes_curso = self._obter_informacoes_curso()
        nome_curso = informacoes_curso["titulo"]

        nome = self._gerar_texto_aleatorio(
            "Crie um nome aleatório (máximo 3 palavras)")
        comentario = self._gerar_texto_aleatorio(
            f"Crie um feedback aleatório para o curso chamado {nome_curso} (máximo 100 caracteres)")
        email = self._gerar_texto_aleatorio(
            f"Crie um endereço de email aleatório para a pessoa {nome}")

        nova_descricao = {
            "nome": nome,
            "avaliacao": randint(1, 5),
            "curso": self.id_curso,
            "comentario": comentario,
            "email": email
        }

        result = requests.post(
            url=self.url2, data=nova_descricao, headers=self.headers)

        return result.status_code, nova_descricao


teste = CriarAvaliacao(6)
print(teste.gerar_avaliacao())
