import requests
# Definir o nome para consulta 
nome = input('Digite o nome da pessoa').strip()

url = f'https://apify.io/?name={nome}'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f'NOme: {dados['name']}')
    print(f'Idade estimada: {dados['age']} anos')
    print(f'Número de registros analisando: {dados['count']}')

else:
    print(f'Erro ao acessar a API {response.status_code}')