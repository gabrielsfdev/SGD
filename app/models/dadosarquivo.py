from sqlalchemy import Column, Integer, ForeignKey, TEXT, String
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela DadosArquivo
class DadosArquivoBD(Base):
    __tablename__ = 'dadosarquivo'
    id = Column(Integer, primary_key=True)
    idarquivo = Column(Integer, ForeignKey('arquivo.id'))
    conteudo_arquivo = Column(TEXT)
    contratante = Column(String(200))
    contratada = Column(String(200))
    num_processo = Column(String(100))
    arquivo = relationship('ArquivoBD', back_populates='dadosarquivo')