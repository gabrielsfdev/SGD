from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models import UsuarioBD, TelefoneBD, EnderecoBD, CidadeBD
from app.database import SessionLocal

class AtualizaCadastro:
    def atualiza_cadastro(self, dados_atuais, novos_dados):
        session = SessionLocal()
        
        chaves_usuario = ['nome_usuario', 'datanascimento', 'cpf_usuario']
        chaves_telefone = ['numero_telefone']
        chaves_endereco = ['cep', 'logradouro', 'numero', 'complemento', 'bairro']
        
        try:
            atualizacoes = {
                'usuario': self.atualiza_usuario(session, dados_atuais, novos_dados, chaves_usuario),
                'telefone': self.atualiza_telefone(session, dados_atuais, novos_dados, chaves_telefone),
                'endereco': self.atualiza_endereco(session, dados_atuais, novos_dados, chaves_endereco)
            }
            
            if any(atualizacoes.values()):
                session.commit()
                return "Atualizações realizadas com sucesso."
            else:
                return "Nenhum dado precisou ser atualizado."

        except SQLAlchemyError as e:
            session.rollback()
            return f"Erro durante a atualização: {str(e)}"
        finally:
            session.close()

    def atualiza_usuario(self, session, dados_atuais, novos_dados, chaves_usuario):
        usuario = session.query(UsuarioBD).filter_by(id=dados_atuais.idusuario).first()
        if usuario:
            return self.atualizar_entidade(usuario, dados_atuais, novos_dados, chaves_usuario)
        return False

    def atualiza_telefone(self, session, dados_atuais, novos_dados, chaves_telefone):
        telefone = session.query(TelefoneBD).filter_by(id=dados_atuais.idtelefone).first()
        if telefone:
            return self.atualizar_entidade(telefone, dados_atuais, novos_dados, chaves_telefone)
        return False

    def atualiza_endereco(self, session, dados_atuais, novos_dados, chaves_endereco):
        endereco = session.query(EnderecoBD).filter_by(id=dados_atuais.idendereco).first()
        if endereco:
            foi_atualizado = self.atualizar_entidade(endereco, dados_atuais, novos_dados, chaves_endereco)

            if dados_atuais.nome_cidade != novos_dados['nome_cidade']:
                cidade = session.query(CidadeBD).filter_by(nome_cidade=novos_dados['nome_cidade']).first()
                if cidade:
                    endereco.idcidade = cidade.id
                    return True
            return foi_atualizado
        return False

    def atualizar_entidade(self, entidade, dados_atuais, novos_dados, chaves):
        atualizado = False
        for chave in chaves:
            if getattr(dados_atuais, chave) != novos_dados[chave]:
                setattr(entidade, chave, novos_dados[chave])
                atualizado = True
        return atualizado
