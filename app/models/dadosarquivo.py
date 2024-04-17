from sqlalchemy import Column, Integer, ForeignKey, TEXT
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela DadosArquivo
class DadosArquivoBD(Base):
    __tablename__ = 'dadosarquivo'
    id = Column(Integer, primary_key=True)
    idarquivo = Column(Integer, ForeignKey('arquivo.id'))
    resumo_arquivo = Column(TEXT)
    conteudo_arquivo = Column(TEXT)
    arquivo = relationship('ArquivoBD', back_populates='dadosarquivo')