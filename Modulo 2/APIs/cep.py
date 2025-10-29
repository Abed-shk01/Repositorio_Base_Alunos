# Crie um api que consulte o cep e informe o enddereço


# iniciamos fazendo a importação de biblioteca requests
import requests

cep = input('Digite o CEP (somente números): ').strip() # Usuário informa o cep que deseja consultar
url = f'https://viacep.com.br/ws/{cep}/json/'  # endereço de url formatado para pesquida do cep

# Fazemos a requesição

resposta = requests.get(url) # aqui estamos fazendo a requisição

if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' not in dados:
        print(f'CEP: {dados['cep']}')
        print(f'Logradouro: {dados['cep']}')
        print(f'Bairro: {dados['bairro']}')
        print(f'cidade: {dados['localidade']}')
        print(f'Estado: {dados['uf']}')
    else:
        print('CEP não foi encontrado')
else:
    print(f'O erro na requisição {resposta.status_code}')
    print(resposta.content)
