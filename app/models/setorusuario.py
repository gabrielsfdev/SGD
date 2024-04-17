from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela SetorUsuario
class SetorUsuarioBD(Base):
    __tablename__ = 'setorusuario'
    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey('usuario.id'))
    idsetor = Column(Integer, ForeignKey('setor.id'))
    usuario = relationship('UsuarioBD', back_populates='setorusuario')
    setor = relationship('SetorBD', back_populates='setorusuario')
    
    __table_args__ = (UniqueConstraint('idusuario', 'idsetor', name='unique_usuario_setor'),)