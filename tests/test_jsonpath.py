import jsonpath
import requests


avaliacoes_get = requests.get("http://localhost:8000/api/v2/avaliacoes/")
data = avaliacoes_get.json()

results = jsonpath.jsonpath(data, "results")
name = jsonpath.jsonpath(data, "results[0].nome")
names = jsonpath.jsonpath(data, "results[*].nome")


# print(name)
# print(results)
print(names)
