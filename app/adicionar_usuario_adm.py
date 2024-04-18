import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))
from sqlalchemy.orm import sessionmaker
from app import engine
from app.services import Usuario

Session = sessionmaker(bind=engine)
session = Session()

def cadastra_adm():
    usuario_adm = {
        'nome_usuario': 'Administrador SGD',
        'cpf_usuario': '914.400.480-02',
        'datanascimento': '1988-01-01',
        'login': 'admin',
        'senha': 'admin@123456#',
        'telefone': '(11)99999-9999',
        'email': 'admin@sgd.com.br',
        'cep': '72804-210',
        'logradouro': 'Rua Guimarães Rosa',
        'numero': '14',
        'complemento': 'QD 57',
        'bairro': 'Parque Estrela Dalva I',
        'cidade': 'Luziânia',
        'idperfil': 1
        }
    
    usuario = Usuario(
        nome = usuario_adm['nome_usuario'],
        cpf = usuario_adm['cpf_usuario'],
        datanascimento = usuario_adm['datanascimento'],
        login = usuario_adm['login'],
        senha = usuario_adm['senha']
        )
    
    usuario.registrar_usuario(
        telefone = usuario_adm['telefone'],
        email = usuario_adm['email'],
        cep = usuario_adm['cep'],
        logradouro = usuario_adm['logradouro'],
        numero = usuario_adm['numero'],
        complemento = usuario_adm['complemento'],
        bairro = usuario_adm['bairro'],
        cidade = usuario_adm['cidade'],
        idperfil = 1
    )