from sqlalchemy import Column, Integer, ForeignKey, TEXT, String, DateTime
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela DadosDocumento
class DadosDocumentoBD(Base):
    __tablename__ = 'dadosdocumento'
    id = Column(Integer, primary_key=True)
    idarquivo = Column(Integer, ForeignKey('arquivo.id'))
    nome_documento = Column(String(200))
    numero_rg = Column(String(50))
    data_nascimento = Column(DateTime)
    nome_mae = Column(String(200))
    local_nascimento = Column(String(200))
    arquivo = relationship('ArquivoBD', back_populates='dadosdocumento')