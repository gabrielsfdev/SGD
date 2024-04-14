from sqlalchemy import Column, Integer, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela ArquivoBlob
class ArquivoBlobBD(Base):
    __tablename__ = 'arquivoblob'
    id = Column(Integer, primary_key=True)
    idarquivo = Column(Integer, ForeignKey('arquivo.id'))
    blob_dados = Column(LargeBinary)
    arquivo = relationship('ArquivoBD', back_populates='arquivo')