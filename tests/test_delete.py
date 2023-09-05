import requests

headers = {
    "Authorization": "Token 46a48747c49fa70c69c33a7bdf886f0fdd6fe1f0"
}

cursos_base = "http://localhost:8000/api/v2/cursos/"
avaliacoes_base = "http://localhost:8000/api/v2/avaliacoes/"


resultado = requests.delete(url=f'{cursos_base}2/', headers=headers)

assert resultado.status_code == 204
