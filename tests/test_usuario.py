import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))

from app.services import Usuario
from app.utils import *
from datetime import datetime
import json

def test_registrar_usuario(nome, cpf, data_nascimento, email, telefone, cep, logradouro, numero, complemento, bairro, cidade, login, senha):
    usuario = Usuario(
        nome = nome,
        cpf = cpf,
        datanascimento = data_nascimento,
        login = login,
        senha = senha
    )
    resultado = usuario.registrar_usuario(
        telefone = telefone,
        email = email,
        cep = cep,
        logradouro = logradouro,
        numero = numero,
        complemento = complemento,
        bairro = bairro,
        cidade = cidade
    )
    print(resultado)

if __name__ == "__main__":
    nome = input('Informe o nome: ')
    
    while True:
        cpf = input('Informe o CPF (Apenas Números): ')
        try:
            cpf_validado = valida_cpf(cpf)
            break
        except ValueError as e:
            print(e)
    
    data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        data_nascimento = data_nascimento.strftime("%Y-%m-%d")
    except ValueError:
        print("Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")
    
    email = input('Informe o email: ')
    telefone = input('Informe o telefone com DDD: ')
    
    while True:
        cep = input('Informe o CEP com 8 números: ')
        try:
            dados_cep = busca_cep(cep)
            break
        except ValueError as e:
            print(e)
            
    if dados_cep.status_code == 200:
        json_cep = json.loads(dados_cep.content.decode('utf-8'))
        cep = json_cep['cep']
        logradouro = json_cep['logradouro']
        bairro = json_cep['bairro']
        cidade = json_cep['localidade']
        numero = input('Informe o número da residencia: ')
        complemento = input('Informe o complemento: ')
    else:
        logradouro = input('Informe o logradouro (Rua, Avenida, etc): ')
        numero = input('Informe o número da residencia: ')
        complemento = input('Informe o complemento: ')
        bairro = input('Informe o bairro: ')
        cidade = input('Informe a cidade: ')
    
    login = input('Informe o login: ')
    senha = input('Informe a senha: ')
    
    test_registrar_usuario(nome, cpf_validado, data_nascimento, email, telefone, cep, logradouro, numero, complemento, bairro, login, senha)
