import requests

headers = {
    "Authorization": "Token 46a48747c49fa70c69c33a7bdf886f0fdd6fe1f0"
}

cursos_base = "http://localhost:8000/api/v2/cursos/"
avaliacoes_base = "http://localhost:8000/api/v2/avaliacoes/"


novo_curso = {
    "titulo": "aprendendo API 2",
    "url": "https://www.api2.com.br"
}

resultado = requests.put(url=f'{cursos_base}2/',
                         data=novo_curso, headers=headers)

assert resultado.status_code == 200

assert resultado.json()["titulo"] == novo_curso["titulo"]
