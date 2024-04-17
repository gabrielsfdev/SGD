from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela ArquivoUsuario
class ArquivoUsuarioBD(Base):
    __tablename__ = 'arquivousuario'
    id = Column(Integer, primary_key=True)
    idarquivo = Column(Integer, ForeignKey('arquivo.id'))
    idusuario = Column(Integer, ForeignKey('usuario.id'))
    arquivo = relationship('ArquivoBD', back_populates='arquivousuario')
    usuario = relationship('UsuarioBD', back_populates='arquivousuario')