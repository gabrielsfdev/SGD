from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

#Modelo da tabela Setor
class SetorBD(Base):
    __tablename__ = 'setor'
    id = Column(Integer, primary_key=True)
    nome_setor = Column(String(50))
    datacadastro_setor = Column(DateTime, default=datetime.now())
    arquivos = relationship('ArquivoBD', back_populates='setor')
    arquivosetor = relationship('ArquivoSetorBD', back_populates='setor')
    setorusuario = relationship('SetorUsuarioBD', back_populates='setor')