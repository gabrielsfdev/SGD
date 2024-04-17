from sqlalchemy import Column, Integer, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela EscritorioUsuario
class EscritorioUsuarioBD(Base):
    __tablename__ = 'escritoriousuario'
    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey('usuario.id'))
    idescritorio = Column(Integer, ForeignKey('escritorio.id'))
    gestor = Column(Boolean, default=False)
    usuario = relationship('UsuarioBD', back_populates='escritoriousuario')
    escritorio = relationship('EscritorioBD', back_populates='escritoriousuario')
    
    __table_args__ = (UniqueConstraint('idusuario', 'idescritorio', name='unique_usuario_escritorio'),)