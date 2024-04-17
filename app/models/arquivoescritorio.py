from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela ArquivoEscritorio
class ArquivoEscritorioBD(Base):
    __tablename__ = 'arquivoescritorio'
    id = Column(Integer, primary_key=True)
    idarquivo = Column(Integer, ForeignKey('arquivo.id'))
    idescritorio = Column(Integer, ForeignKey('escritorio.id'))
    arquivo = relationship('ArquivoBD', back_populates='arquivoescritorio')
    escritorio = relationship('EscritorioBD', back_populates='arquivoescritorio')