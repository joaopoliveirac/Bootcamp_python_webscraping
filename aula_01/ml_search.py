import requests
from bs4 import BeautifulSoup
import pandas as pd

keyword = 'Sabonete'
url = f'https://lista.mercadolivre.com.br/{keyword}'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') #pegar o texto que recebi e transformar em um html
    search_result = soup.find_all('li', class_ = 'ui-search-layout__item') #vou pegar todas as divs que tem essa classe

    data = []
    for result in search_result: 
        link = result.find("a", class_ ="poly-component__title")
        data.append({'Link': link})
    
    print(data)
else:
    print('erro')