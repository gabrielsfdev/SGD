from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela ArquivoSetor
class ArquivoSetorBD(Base):
    __tablename__ = 'arquivosetor'
    id = Column(Integer, primary_key=True)
    idarquivo = Column(Integer, ForeignKey('arquivo.id'))
    idsetor = Column(Integer, ForeignKey('setor.id'))
    arquivo = relationship('ArquivoBD', back_populates='arquivosetor')
    setor = relationship('SetorBD', back_populates='arquivosetor')