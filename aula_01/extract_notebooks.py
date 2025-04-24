import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

contador = 1
data = []

for i in range(0,10):
    if contador == 1:
        keyword = 'notebook'
        url = f'https://lista.mercadolivre.com.br/{keyword}'
    else:
        url = f'https://lista.mercadolivre.com.br/informatica/portateis-acessorios/notebooks/notebook_Desde_{contador}_NoIndex_True'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser') #pegar o texto que recebi e transformar em um html
        search_result = soup.find_all('li', class_ = 'ui-search-layout__item') #vou pegar todas as divs que tem essa classe

        for result in search_result:
            title = result.find("h3", class_ ="poly-component__title-wrapper").text.strip()
            marca = result.find("span", class_="poly-component__brand")
            if marca is not None:
                marca = result.find("span", class_="poly-component__brand").text.strip()
            else:
                marca = result.find("span", class_="poly-component__brand")
            link_tag = result.find("a", class_="poly-component__title")
            link = link_tag.get('href')
            preco = result.find("span", class_="andes-money-amount andes-money-amount--cents-superscript").text
            data.append({'Title': title, 'Marca': marca, 'Link': link, "Preco": preco})
        
        contador += 48

df = pd.DataFrame(data)
def limpar_string(s):
    if isinstance(s, str):
        return ILLEGAL_CHARACTERS_RE.sub('', s) #identifica caracteres nao permitidos em excel e os remove(substitui qualquer caracter proibido(s) por uma string vazia(''))
    return s
df = df.applymap(limpar_string)
df.to_excel('notebook.xlsx', index=False)

