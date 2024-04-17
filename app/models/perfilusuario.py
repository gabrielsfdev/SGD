from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela PerfilUsuario
class PerfilUsuarioBD(Base):
    __tablename__ = 'perfilusuario'
    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey('usuario.id'))
    idperfil = Column(Integer, ForeignKey('perfil.id'))
    usuario = relationship('UsuarioBD', back_populates='perfilusuario')
    perfil = relationship('PerfilBD', back_populates='perfilusuario')
    
    __table_args__ = (UniqueConstraint('idusuario', 'idperfil', name='unique_usuario_perfil'),)