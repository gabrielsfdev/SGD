import requests

def busca_cep(cep):
    if not cep or len(cep) != 8 or not cep.isdigit():
        raise ValueError("O CEP informado está incorreto. Deve conter 8 números.")
    
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    response = requests.get(url)
    return response