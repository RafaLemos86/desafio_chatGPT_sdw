import requests

# get de avaliacoes

avaliacoes_get = requests.get("http://localhost:8000/api/v2/avaliacoes/")
avaliacao_get = requests.get("http://localhost:8000/api/v2/avaliacoes/2/")


# print(avaliacoes_get.status_code)
# print(avaliacoes_get.json())
# print(avaliacoes_get.json()['results'][0]['comentario'])


headers = {
    "Authorization": "Token 46a48747c49fa70c69c33a7bdf886f0fdd6fe1f0"
}

cursos_get = requests.get(
    url="http://localhost:8000/api/v2/cursos/", headers=headers)

print(cursos_get.json())
