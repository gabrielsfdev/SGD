from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela Telefone
class TelefoneBD(Base):
    __tablename__ = 'telefone'
    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey('usuarios.id'))
    telefone = Column(String(14))
    usuario = relationship('UsuarioBD', back_populates='telefones')