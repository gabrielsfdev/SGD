from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

#Modelo da tabela Arquivo
class ArquivoBD(Base):
    __tablename__ = 'arquivo'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    idusuario = Column(Integer, ForeignKey('usuarios.id'))
    idsetor = Column(Integer, ForeignKey('setor.id'), nullable=True)
    idescritorio = Column(Integer, ForeignKey('escritorio.id'), nullable=True)
    datacriacao = Column(DateTime, default=datetime.now())
    restricao = Column(Boolean, default=False)
    tipo = Column(String(10))
    tamanho = Column(Integer)
    usuario = relationship('UsuarioBD', back_populates='arquivos')
    setor = relationship('SetorBD', back_populates='arquivos')
    escritorio = relationship('EscritorioBD', back_populates='arquivos')
    blob = relationship('ArquivoBlobBD', back_populates='arquivo', uselist=False)