from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_
from app.models import ArquivoBD, ArquivoBlobBD
from app.database import SessionLocal
from app.services import Sessao
import os
from datetime import datetime

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
    
    def busca_arquivo(self, **kwargs):
        session = SessionLocal()
        itens_busca = ['nome_arquivo', 'data_inicial', 'data_final', 'nome_documento', 'cpf_documento']
        filtro = []
        
        for item in itens_busca:
            valor = kwargs.get(item)
            if valor:
                if item == 'nome_arquivo':
                    filtro.append(ArquivoBD.nome_arquivo.contains(valor))
                elif item == 'data_inicial':
                    try:
                        data_formatada = datetime.strptime(valor, '%d/%m/%Y').date()
                        filtro.append(ArquivoBD.datacriacao >= data_formatada)
                    except ValueError:
                        return {'success': False, 'message': 'Formato de data inválido para data inicial.'}
                elif item == 'data_final':
                    try:
                        data_formatada = datetime.strptime(valor, '%d/%m/%Y').date()
                        filtro.append(ArquivoBD.datacriacao <= data_formatada)
                    except ValueError:
                        return {'success': False, 'message': 'Formato de data inválido para data final.'}
                elif item == 'nome_documento':
                    filtro.append(ArquivoBD.nome_documento.contains(valor))
                elif item == 'cpf_documento':
                    filtro.append(ArquivoBD.cpf_documento.contains(valor))
        
        if not filtro:
            return {'success': False, 'message': 'Nenhum critério de busca fornecido.'}
        
        busca = session.query(ArquivoBD).filter(or_(*filtro)).all()
        session.close()
        if busca:
            return {'success': True, 'message': 'Arquivos encontrados.', 'arquivos': busca}
        else:
            return {'success': False, 'message': 'Nenhum arquivo encontrado.'}
    
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
