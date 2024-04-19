import json
import os
from app.models import UsuarioBD, EnderecoBD, TelefoneBD, EmailBD, CidadeBD, PerfilUsuarioBD
from app.database import SessionLocal

class Sessao:
    def __init__(self, arquivo="sessao_usuario.json"):
        self.arquivo = arquivo


    # Registra a sessão do usuário durante o login
    def registra_sessao(self, usuario):
        dados_usuario = usuario.dados_usuario()
        with open(self.arquivo, "w") as arquivo:
            json.dump(dados_usuario, arquivo)


    # Carrega os dados do usuário logado
    def carrega_sessao(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as arquivo:
                return json.load(arquivo)
        return None


    # Apaga o arquivo da sessão, deslogando o usuário
    def limpa_sessao(self):
        """Apaga os dados de sessão, removendo o arquivo se existir."""
        try:
            if os.path.exists(self.arquivo):
                os.remove(self.arquivo)
                return not os.path.exists(self.arquivo)
            else:
                return True
        except OSError as e:
            print(f"Erro ao realizar o logoff: {e}")
        return False


    # Valida se existe uma sessão ativa, ou seja, um usuário logado
    def usuario_logado(self):
        """Verifica se existe uma sessão ativa."""
        return os.path.exists(self.arquivo)
    
    
    def valida_perfil(self):
        usuario = self.carrega_sessao()
        idperfil = 3
        if usuario is not None:
            for i in range(len(usuario['perfis'])):
                if usuario['perfis'][i]['idperfil'] == 1:
                    idperfil = 1
                    break
                elif usuario['perfis'][i]['idperfil'] == 2:
                    idperfil = 2
            return idperfil


    def recupera_dados(self):
        dados_sessao = self.carrega_sessao()
        try:
            if dados_sessao is None:
                raise Exception("Usuário não está logado.")
            
            session = SessionLocal()
            usuario = (session.query(UsuarioBD.id.label('idusuario'),
                                    UsuarioBD.nome_usuario,
                                    UsuarioBD.datanascimento,
                                    UsuarioBD.cpf_usuario,
                                    TelefoneBD.id.label('idtelefone'),
                                    TelefoneBD.numero_telefone,
                                    EnderecoBD.id.label('idendereco'),
                                    EnderecoBD.cep,
                                    EnderecoBD.logradouro,
                                    EnderecoBD.numero,
                                    EnderecoBD.complemento,
                                    EnderecoBD.bairro,
                                    CidadeBD.nome_cidade,
                                    CidadeBD.uf
                                    )
                        .join(EmailBD, UsuarioBD.id == EmailBD.idusuario)
                        .join(EnderecoBD, UsuarioBD.id == EnderecoBD.idusuario)
                        .join(TelefoneBD, UsuarioBD.id == TelefoneBD.id)
                        .join(CidadeBD, EnderecoBD.idcidade == CidadeBD.id)
                        .filter(UsuarioBD.id == dados_sessao['id'])
                        .first())
            if usuario:
                return {'success': True, 'message': 'Dados carregados com sucesso!', 'usuario': usuario}
            else:
                return {'success': False, 'message': 'Usuário não encontrado.'}
        except Exception as e:
            return f"Erro ao buscar os dados: {e}"