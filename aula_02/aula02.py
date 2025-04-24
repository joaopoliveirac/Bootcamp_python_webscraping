import requests
import pandas as pd
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

url = "https://api.vendas.gpa.digital/pa/search/search"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}
pagina = 1
payload = {
    "terms": "arroz",
    "page": pagina,
    "sortBy": "relevance",
    "resultsPerPage": 8,
    "allowRedirect": True,
    "storeId": 461,
    "customerPlus": True,
    "department": "ecom",
    "partner": "linx"
}

response = requests.post(url, json=payload, headers=headers)
dados = response.json()
tamanho = dados['totalPages']

lista_dados = []
tratados = []

for i in range(1,tamanho+1):
    payload['page'] = i
    response = requests.post(url, json=payload, headers=headers)
    dados = response.json()
    lista_dados.append(dados)
    for produto in dados['products']:
        #print(produto)
        tratados.append({'nome': produto['name'], 'preco': produto['price']})


df = pd.DataFrame(tratados)
def limpar_string(s):
    if isinstance(s, str):
        return ILLEGAL_CHARACTERS_RE.sub('', s) #identifica caracteres nao permitidos em excel e os remove(substitui qualquer caracter proibido(s) por uma string vazia(''))
    return s
df = df.applymap(limpar_string)
df.to_excel('arroz.xlsx', index=False)
print(df.head())
