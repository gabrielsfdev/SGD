import sys
sys.path.append('D:/Projetos/Python/SGD') #Altere para a raiz do seu projeto

from app.services import Usuario
from datetime import datetime

def test_registrar_usuario(nome, cpf, data_nascimento, email, telefone, logradouro, numero, complemento, bairro, login, senha):
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
        logradouro = logradouro,
        numero = numero,
        complemento = complemento,
        bairro = bairro,
        idcidade = 1
    )
    print(resultado)

if __name__ == "__main__":
    nome = input('Informe o nome: ')
    cpf = input('Informe o CPF: ')
    data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        data_nascimento = data_nascimento.strftime("%Y-%m-%d")
    except ValueError:
        print("Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")
    
    email = input('Informe o email: ')
    telefone = input('Informe o telefone com DDD: ')
    logradouro = input('Informe o logradouro (Rua, Avenida, etc): ')
    numero = input('Informe o número da residencia: ')
    complemento = input('Informe o complemento: ')
    bairro = input('Informe o bairro: ')
    login = input('Informe o login: ')
    senha = input('Informe a senha: ')
    
    test_registrar_usuario(nome, cpf, data_nascimento, email, telefone, logradouro, numero, complemento, bairro, login, senha)
