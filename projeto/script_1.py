import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.mercadolivre.com.br/ofertas#nav-header'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') #pegar o texto que recebi e transformar em um html
    search_result = soup.find_all('div', class_ = 'andes-card') #vou pegar todas as divs que tem essa classe
    produtos = []
    for result in search_result:
        titulo = result.find("a", class_ ="poly-component__title")
        if titulo:
            titulo = titulo.text.strip()
        preco_antigo = result.find('span', class_='andes-money-amount__fraction')
        if preco_antigo:
            preco_antigo = result.find('span', class_='andes-money-amount__fraction').text.strip()
        preco_novo = result.find('span', class_ = 'andes-money-amount andes-money-amount--cents-superscript')
        if preco_novo:
            preco_novo = preco_novo.text.strip()
        desconto = result.find('span', class_ = 'andes-money-amount__discount poly-price__disc_label')
        if desconto:
            desconto = desconto.text.strip()
        else:
            desconto= result.find('span', class_ = 'andes-money-amount__discount')
            if desconto:
                desconto= desconto.text.strip()
                
        
        link = result.find("a", class_ ="poly-component__title")
        if link:
            link = link['href']

        produtos.append({'titulo': titulo, 'preco_antigo' : preco_antigo, 'preco_novo': preco_novo, 'desconto': desconto, 'link': link}) 

df = pd.DataFrame(produtos)
df.to_csv('produtos_pagina_inicial.csv', index=False, float_format="%.3f")

