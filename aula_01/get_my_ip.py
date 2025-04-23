import requests
url = 'http://lumtest.com/myip.json'
url2 = 'https://www.globo.com/'

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print('erro')