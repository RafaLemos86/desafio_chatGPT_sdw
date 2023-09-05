import requests
import jsonpath

headers = {
    "Authorization": "Token 46a48747c49fa70c69c33a7bdf886f0fdd6fe1f0"
}

cursos_base = "http://localhost:8000/api/v2/cursos/"
avaliacoes_base = "http://localhost:8000/api/v2/avaliacoes/"

curso = requests.get(url=cursos_base, headers=headers)

curso_id = jsonpath.jsonpath(curso.json(), 'results.[0].id')
curso_title = jsonpath.jsonpath(curso.json(), "results[0].titulo")


# testando curso com status 200
assert curso.status_code == 200

assert curso_id[0] == 2 and curso_title[0] == "Programação com NodeJS 2.0"
