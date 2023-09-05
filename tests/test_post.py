import requests

headers = {
    "Authorization": "Token 46a48747c49fa70c69c33a7bdf886f0fdd6fe1f0"
}

cursos_base = "http://localhost:8000/api/v2/cursos/"
avaliacoes_base = "http://localhost:8000/api/v2/avaliacoes/"

novo_curso = {
    "titulo": "aprendendo APIII",
    "url": "https://www.apiiii.com.br"
}

criacao = requests.post(url=cursos_base, data=novo_curso, headers=headers)

# print(criacao.status_code)

assert criacao.status_code == 201

assert criacao.json()["url"] == novo_curso["url"]
