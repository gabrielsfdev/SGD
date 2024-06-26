from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import or_, and_, func
from app.models import ArquivoBD, ArquivoBlobBD, DadosDocumentoBD, DadosArquivoBD
from app.database import SessionLocal
from app.services import Sessao
import os
from datetime import datetime, timedelta
from tkinter.filedialog import asksaveasfilename


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
        nome = os.path.basename(caminho_arquivo)
        if nome.split('.')[-1] == 'pdf':
            return self.upload_contrato(caminho_arquivo)
        else:
            return self.upload_documento(caminho_arquivo)
        

    def upload_documento(self, caminho_arquivo):
        # Lê o arquivo e cria os registros no banco
        try:
            id_usuario = self.usuario()
            if not id_usuario:
                raise Exception("Usuário não está logado.")
            
            from app.services import OCR_DOCS
            
            ocr = OCR_DOCS(caminho_arquivo)
            dados = ocr.extract_rg_info()
            
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
                
                if dados['success']:
                
                    dados_documento = DadosDocumentoBD(
                        idarquivo=novo_arquivo.id,
                        nome_documento=dados['dados']['nome_documento'],
                        numero_rg=dados['dados']['numero_rg'],
                        data_nascimento=dados['dados']['data_nascimento'],
                        nome_mae=dados['dados']['nome_mae'],
                        local_nascimento=dados['dados']['local_nascimento'],
                    )

                    self.db_session.add(dados_documento)

                self.db_session.commit()
                
                return {'success': True, 'message': 'Arquivo salvo com sucesso!', 'nome': nome}

        except Exception as e:
            self.db_session.rollback()
            return f"Erro ao fazer upload do arquivo: {e}"
    
    def upload_contrato(self, caminho_arquivo):
        # Lê o arquivo e cria os registros no banco
        try:
            id_usuario = self.usuario()
            if not id_usuario:
                raise Exception("Usuário não está logado.")
            
            from app.services import OCR_DOCS
            
            ocr = OCR_DOCS(caminho_arquivo)
            dados = ocr.extract_contract_info()
            
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
                
                if dados['success']:
                
                    dados_contrato = DadosArquivoBD(
                        idarquivo=novo_arquivo.id,
                        conteudo_arquivo=dados['dados']['conteudo'],
                        contratante=dados['dados']['contratante'],
                        contratada=dados['dados']['contratada'],
                        num_processo=dados['dados']['num_processo'],
                    )

                    self.db_session.add(dados_contrato)

                self.db_session.commit()
                
                return {'success': True, 'message': 'Arquivo salvo com sucesso!', 'nome': nome}

        except Exception as e:
            self.db_session.rollback()
            return f"Erro ao fazer upload do arquivo: {e}"
    
    def busca_documento(self, **kwargs):
        session = SessionLocal()
        try:
            filtro_arquivo = []
            filtro_documento = []

            for chave, valor in kwargs.items():
                if valor:
                    valor = valor.strip()
                    if chave == 'nome_arquivo':
                        filtro_arquivo.append(func.lower(ArquivoBD.nome_arquivo).contains(valor.lower()))
                    elif chave in ['data_inicial', 'data_final']:
                        try:
                            data_formatada = datetime.strptime(valor, '%d/%m/%Y').date()
                            if chave == 'data_inicial':
                                filtro_arquivo.append(ArquivoBD.datacriacao >= data_formatada) 
                            else:
                                data_formatada = datetime.strptime(valor, '%d/%m/%Y') + timedelta(days=1, microseconds=-1)
                                filtro_arquivo.append(ArquivoBD.datacriacao <= data_formatada)
                        except ValueError:
                            return {'success': False, 'message': f'Formato de data inválido para {chave}.'}
                    elif chave == 'nome_documento':
                        filtro_documento.append(func.lower(DadosDocumentoBD.nome_documento).contains(valor.lower()))
                    elif chave == 'numero_rg':
                        filtro_documento.append(DadosDocumentoBD.numero_rg.contains(valor))
                    elif chave == 'data_nascimento':
                        try:
                            data_formatada = datetime.strptime(valor, '%d/%m/%Y').date()
                            filtro_documento.append(DadosDocumentoBD.data_nascimento == data_formatada)
                        except ValueError:
                            return {'success': False, 'message': f'Formato de data inválido para {chave}.'}
                    elif chave == 'nome_mae':
                        filtro_documento.append(func.lower(DadosDocumentoBD.nome_mae).contains(valor.lower()))
                    elif chave == 'local_nascimento':
                        filtro_documento.append(func.lower(DadosDocumentoBD.local_nascimento).contains(valor.lower()))

            if not filtro_arquivo and not filtro_documento:
                return {'success': False, 'message': 'Nenhum critério de busca fornecido.'}

            busca = (session.query(ArquivoBD.id, ArquivoBD.nome_arquivo, DadosDocumentoBD.nome_documento.label('nome_pessoa'), ArquivoBD.datacriacao)
                            .join(DadosDocumentoBD, ArquivoBD.id == DadosDocumentoBD.idarquivo)
                            .filter(and_(or_(*filtro_arquivo), or_(*filtro_documento)))
                            .all())

            if busca:
                return {'success': True, 'message': 'Arquivos encontrados.', 'arquivos': busca}
            else:
                return {'success': False, 'message': 'Nenhum arquivo encontrado.'}

        except SQLAlchemyError as e:
            session.rollback()
            return {'success': False, 'message': f'Erro ao acessar banco de dados: {str(e)}'}
        finally:
            session.close()

            if busca:
                return {'success': True, 'message': 'Arquivos encontrados.', 'arquivos': busca}
            else:
                return {'success': False, 'message': 'Nenhum arquivo encontrado.'}


    def busca_contrato(self, **kwargs):
        session = SessionLocal()
        try:
            filtro_arquivo = []
            filtro_contrato = []
            stop_words = set(['de', 'para', 'a', 'o', 'as', 'os', 'e', 'do', 'da', 'dos', 'das', 'um', 'uma'])

            for chave, valor in kwargs.items():
                if valor:
                    valor = valor.strip()
                    if chave == 'nome_arquivo':
                        filtro_arquivo.append(func.lower(ArquivoBD.nome_arquivo).contains(valor.lower()))
                    elif chave in ['data_inicial', 'data_final']:
                        try:
                            data_formatada = datetime.strptime(valor, '%d/%m/%Y').date()
                            if chave == 'data_inicial':
                                filtro_arquivo.append(ArquivoBD.datacriacao >= data_formatada) 
                            else:
                                data_formatada = datetime.strptime(valor, '%d/%m/%Y') + timedelta(days=1, microseconds=-1)
                                filtro_arquivo.append(ArquivoBD.datacriacao <= data_formatada)
                        except ValueError:
                            return {'success': False, 'message': f'Formato de data inválido para {chave}.'}
                    elif chave == 'partes_contrato':
                        filtro_arquivo.append(
                            or_(
                                func.lower(DadosArquivoBD.contratada).contains(valor.lower()),
                                func.lower(DadosArquivoBD.contratante).contains(valor.lower())
                            )
                        )
                    elif chave == 'num_processo':
                        filtro_arquivo.append(DadosArquivoBD.num_processo.contains(valor))
                    elif chave == 'conteudo_arquivo':
                        filtro_contrato.append(func.lower(DadosArquivoBD.conteudo_arquivo).contains(valor.lower()))
                        palavras = valor.split()
                        palavras_chave = [palavra for palavra in palavras if palavra.lower() not in stop_words]
                        if len(palavras_chave) > 1:
                            for palavra in palavras_chave:
                                filtro_contrato.append(func.lower(DadosArquivoBD.conteudo_arquivo).contains(palavra.lower()))

            if not filtro_arquivo and not filtro_contrato:
                return {'success': False, 'message': 'Nenhum critério de busca fornecido.'}
            
            if filtro_arquivo and filtro_contrato:
                # Ambos os filtros contêm condições
                condicao_final = and_(and_(*filtro_arquivo), or_(*filtro_contrato))
            elif filtro_arquivo:
                # Apenas filtro_arquivo contém condições
                condicao_final = and_(*filtro_arquivo)
            elif filtro_contrato:
                # Apenas filtro_contrato contém condições
                condicao_final = or_(*filtro_contrato)

            busca = (session.query(
                    ArquivoBD.id,
                    ArquivoBD.nome_arquivo,
                    DadosArquivoBD.num_processo,
                    ArquivoBD.datacriacao)
                    .join(DadosArquivoBD, ArquivoBD.id == DadosArquivoBD.idarquivo)
                    .filter(condicao_final)
                    .all())

            if busca:
                return {'success': True, 'message': 'Arquivos encontrados.', 'arquivos': busca}
            else:
                return {'success': False, 'message': 'Nenhum arquivo encontrado.'}

        except SQLAlchemyError as e:
            session.rollback()
            return {'success': False, 'message': f'Erro ao acessar banco de dados: {str(e)}'}
        finally:
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
                # Abre a janela de diálogo para salvar arquivo
                caminho = asksaveasfilename(defaultextension=".pdf",
                                            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
                                            initialfile=nome)
                if not caminho:
                    return {'success': False, 'message': 'Download cancelado pelo usuário.'}
                
                with open(caminho, 'wb') as f:
                    f.write(busca.blob_dados)
                
                return {'success': True, 'message': 'Arquivo salvo com sucesso!', 'caminho': caminho}
            else:
                return {'success': False, 'message': 'Nenhum arquivo encontrado.'}
        finally:
            session.close()
