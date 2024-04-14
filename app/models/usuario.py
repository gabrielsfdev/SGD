from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela Usuario
class UsuarioBD(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(200))
    cpf = Column(String(14))
    datanascimento = Column(DateTime)
    login = Column(String(30), unique=True)
    senha = Column(String(200))
    telefones = relationship('TelefoneBD', back_populates='usuario')
    emails = relationship('EmailBD', back_populates='usuario')
    enderecos = relationship('EnderecoBD', back_populates='usuario')
    arquivos = relationship('ArquivoBD', back_populates='usuario')
    
    def dados_usuario(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'login': self.login,
            'data_nascimento': self.datanascimento.strftime('%Y-%m-%d') if self.datanascimento else None,
            'cpf': self.cpf
        }