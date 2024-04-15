import os
import sys
sys.path.append(os.getenv('CAMINHO_RAIZ_PROJETO'))

from app.services import Usuario, Sessao
from app.utils import *
from test_upload import main_upload

def main():
    sessao = Sessao()
    if sessao.usuario_logado():
        usuario = sessao.carrega_sessao()
        print(f"Bem-vindo {usuario['nome']}!")
    else:
        login = fazer_login()
        sessao.registra_sessao(login)
        print("Usuário logado com sucesso!")
    
    return sessao


def fazer_login():
    login = input('Informe seu login ou e-mail: ')
    senha = input('Informe sua senha: ')
    
    usuario = Usuario(login, senha)
    
    realizar_login = usuario.login_usuario()
    
    print(realizar_login['message'])
    
    if realizar_login['success']:
        print(f'Bem vindo {realizar_login['usuario'].nome}')
        return realizar_login['usuario']
    

if __name__ == "__main__":
    sessao = main()
    
    opcao = int(input('Digite 1 para fazer um upload e 0 para fazer LOGOUT: '))
    
    if opcao == 0 and sessao.usuario_logado():
        if sessao.limpa_sessao():
            print('Logout realizado com sucesso.')
        else:
            print('Erro ao realizar o logout. Tente novamente.')
    elif opcao == 1:
        main_upload()