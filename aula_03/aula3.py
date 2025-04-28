import requests
from bs4 import BeautifulSoup

with requests.Session() as s:



    login_url = 'https://www.codechef.com/api/codechef/login'

    context = s.get(login_url)

    soup = BeautifulSoup(context.content, 'html.parser')
    csrf_token = soup.find_all('input')[3]['value']
    cleaned_toekn = csrf_token.replace('\\"', '')
    form_id = soup.find_all('input')[4]['value']
    cleaned_form_id = form_id.replace('\\', '')




    url = 'https://www.codechef.com/api/codechef/login'

    payload = {'name': 'joaopo.0607@gmail.com',
            'pass': '5867213aA@',
            'csrfToken': cleaned_toekn,
            'form_build_id': cleaned_form_id,
            'form_id': 'ajax_login_form'}

    response = s.post(url, data=payload)
    print(response.json())

# porque abrir uma sessão com requests.Session() tem vantagens importantes quando você precisa fazer múltiplas requisições para o mesmo site — como no seu exemplo de fazer um GET para buscar o token e depois um POST para fazer login.

# Principais motivos de usar Session + with:

# Persistência de cookies e headers:

# Quando você usa uma Session(), o Python guarda cookies automaticamente (por exemplo, cookies de login, sessão de usuário) entre as requisições.

# Se você usar requests.get e requests.post separados (sem Session), os cookies de login se perderiam.

# Reutilização de conexão (mais rápido):

# Uma Session mantém a mesma conexão TCP aberta para o mesmo host, o que deixa seu scraping muito mais rápido e eficiente.

# Organização e limpeza automática com with:

# Usando o with, quando você sai do bloco, a sessão é automaticamente fechada (sem precisar chamar s.close() manualmente).

# Isso evita vazamento de conexão (melhor prática).

# Simplificando:


# Sem Session	Com Session
# Cada request é isolado	Cookies e headers persistem
# Conexões mais lentas	Conexões otimizadas
# Mais chance de erro em login	Login e ações subsequentes funcionam melhor