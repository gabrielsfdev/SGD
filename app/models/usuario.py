from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.models import Base
from datetime import datetime

#Modelo da tabela Usuario
class UsuarioBD(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome_usuario = Column(String(200))
    cpf_usuario = Column(String(14), unique=True)
    datanascimento = Column(DateTime)
    login = Column(String(30), unique=True)
    senha = Column(String(200))
    datacadastro_usuario = Column(DateTime, default=datetime.now())
    dataalteracao_usuario = Column(DateTime, nullable=True)
    telefones = relationship('TelefoneBD', back_populates='usuario')
    emails = relationship('EmailBD', back_populates='usuario')
    enderecos = relationship('EnderecoBD', back_populates='usuario')
    arquivos = relationship('ArquivoBD', back_populates='usuario')
    arquivousuario = relationship('ArquivoUsuarioBD', back_populates='usuario')
    perfilusuario = relationship('PerfilUsuarioBD', back_populates='usuario')
    setorusuario = relationship('SetorUsuarioBD', back_populates='usuario')
    escritoriousuario = relationship('EscritorioUsuarioBD', back_populates='usuario')
    
    def dados_usuario(self):
        return {
            'id': self.id,
            'nome_usuario': self.nome_usuario,
            'login': self.login,
            'data_nascimento': self.datanascimento.strftime('%Y-%m-%d') if self.datanascimento else None,
            'cpf_usuario': self.cpf_usuario
        }