import requests


class TestCursos:
    headers = {
        "Authorization": "Token 46a48747c49fa70c69c33a7bdf886f0fdd6fe1f0"
    }

    cursos_base = "http://localhost:8000/api/v2/cursos/"

    def test_get_cursos(self):
        result = requests.get(url=self.cursos_base, headers=self.headers)

        assert result.status_code == 200

    def test_get_curso(self):
        result = requests.get(
            url=f'{self.cursos_base}2/', headers=self.headers)

        assert result.status_code == 200

    def test_post_curso(self):
        novo_curso = {
            "titulo": "testando api com pytest2",
            "url": "https://www.testandoapipytest2.com"
        }

        result = requests.post(url=self.cursos_base,
                               headers=self.headers, data=novo_curso)

        assert result.status_code == 201 and result.json()[
            'titulo'] == novo_curso["titulo"]

    def test_put_curso(self):
        novo_curso = {
            "titulo": "update api",
            "url": "https://www.api13.com.br"
        }

        result = requests.put(
            url=f'{self.cursos_base}2/', headers=self.headers, data=novo_curso)

        assert result.status_code == 200 and result.json()[
            'titulo'] == novo_curso["titulo"]

    def test_delete_curso(self):
        result = requests.delete(
            url=f'{self.cursos_base}5/', headers=self.headers)

        assert result.status_code == 204
