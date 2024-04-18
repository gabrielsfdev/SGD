from sqlalchemy.exc import IntegrityError
from app.models import ArquivoBD, ArquivoBlobBD
from app.database import SessionLocal
from app.services import Sessao
import os

class Arquivo:
    def __init__(self):
        self.db_session =  SessionLocal()
    
    def usuario(self):
        try:
            sessao = Sessao()
            if sessao.usuario_logado():
                sessao_usuario = sessao.carrega_sessao()
                return sessao_usuario['id']
        except Exception as e:
            print(f"Necessário estar logado para fazer um upload: {e}")
            return None

    def upload_arquivo(self, caminho_arquivo):
        # Lê o arquivo e cria os registros no banco
        try:
            id_usuario = self.usuario()
            if not id_usuario:
                raise Exception("Usuário não está logado.")
            
            with open(caminho_arquivo, 'rb') as arquivo:
                dados_arquivo = arquivo.read()
                tamanho = os.path.getsize(caminho_arquivo)
                nome = os.path.basename(caminho_arquivo)
                tipo = nome.split('.')[-1]

                novo_arquivo = ArquivoBD(nome_arquivo=nome, idusuario=id_usuario, tipo_arquivo=tipo, tamanho_arquivo=tamanho)
                self.db_session.add(novo_arquivo)
                self.db_session.flush()

                blob_arquivo = ArquivoBlobBD(idarquivo=novo_arquivo.id, blob_dados=dados_arquivo)
                self.db_session.add(blob_arquivo)

                self.db_session.commit()
                
                return {'success': True, 'message': 'Arquivo salvo com sucesso!', 'nome': nome}

        except Exception as e:
            self.db_session.rollback()
            return f"Erro ao fazer upload do arquivo: {e}"
    
    def busca_arquivo(self, param_busca, texto):
        session = SessionLocal()
        try:
            if hasattr(ArquivoBD, param_busca):
                filtro = getattr(ArquivoBD, param_busca)
                busca = session.query(ArquivoBD).filter(filtro.contains(texto)).all()
                if busca:
                    return {'success': True, 'message': 'Arquivos encontrados.', 'arquivos': busca}
                else:
                    return {'success': False, 'message': 'Nenhum arquivo encontrado.'}
            else:
                return {'success': False, 'message': 'Coluna de busca inválida.'}
        finally:
            session.close()
    
    def download_arquivo(self, id, nome):
        session = SessionLocal()
        try:
            busca = session.query(ArquivoBlobBD).filter(ArquivoBlobBD.idarquivo == id).first()
            if busca:
                print("Por favor, informe o caminho completo onde deseja salvar o arquivo:")
                caminho = input("Caminho: ")
                if not caminho:
                    return {'success': False, 'message': 'Caminho não fornecido. Download cancelado.'}
                
                if caminho[-1] != '\\':
                    caminho += '\\'

                caminho += nome

                with open(caminho, 'wb') as f:
                    f.write(busca.blob_dados)

                return {'success': True, 'message': 'Arquivo salvo com sucesso!', 'caminho': caminho}
            else:
                return {'success': False, 'message': 'Nenhum arquivo encontrado.'}
        finally:
            session.close()
