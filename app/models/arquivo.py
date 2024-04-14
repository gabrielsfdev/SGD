from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela Arquivo
class ArquivoBD(Base):
    __tablename__ = 'arquivo'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    idusuario = Column(Integer, ForeignKey('usuarios.id'))
    idsetor = Column(Integer, ForeignKey('setor.id'), nullable=True)
    idescritorio = Column(Integer, ForeignKey('escritorio.id'), nullable=True)
    datacriacao = Column(DateTime)
    restricao = Column(bool, default=False)
    tipo = Column(String(10))
    tamanho = Column(Integer)
    usuario = relationship('UsuarioBD', back_populates='usuario')
    setor = relationship('SetorBD', back_populates='setor')
    escritorio = relationship('EscritorioBD', back_populates='escritorio')