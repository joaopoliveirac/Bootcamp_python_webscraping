import requests
from bs4 import BeautifulSoup
import pandas as pd

def requisicao(pagina, resultado_por_pagina, item):
    url = 'https://api.vendas.gpa.digital/pa/search/search'
    headers = {
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    payload = {
        "terms": item,
        "page": pagina or 1,
        "sortBy": "relevance",
        "resultsPerPage": resultado_por_pagina,
        "allowRedirect": True,
        "storeId": 461,
        "customerPlus": True,
        "department": "ecom",
        "partner": "linx"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    except Exception as e:
        print(f"Erro na requisição: {e}")
        return None

def tratar(dados_iniciais, resultado_por_pagina=50, item=''):
    produtos = []
    total_produtos = dados_iniciais.get('totalProducts', 0)
    pagina = 1

    while len(produtos) < total_produtos:
        dados = requisicao(pagina, resultado_por_pagina, item)

        if not dados or 'products' not in dados:
            break

        for produto in dados['products']:
            nome = produto['name']
            preco = produto['price']
            link = produto['urlDetails']
            vendedor = produto['sellerName']
            produtos.append({
                'nome': nome,
                'preco': preco,
                'link': link,
                'vendedor': vendedor
            })

        pagina += 1

    return produtos

# Execução principal
item_busca = 'azeite'
resultado_por_pagina = 50

dados_iniciais = requisicao(1, resultado_por_pagina, item_busca)
if dados_iniciais:
    tratamento = tratar(dados_iniciais, resultado_por_pagina, item_busca)
    df = pd.DataFrame(tratamento)
    print(df.head())
    df.to_csv(f'{item_busca}.csv', index=False)
else:
    print("Não foi possível obter os dados iniciais.")
