from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela Email
class EmailBD(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey('usuarios.id'))
    email = Column(String(100), unique=True)
    usuario = relationship('UsuarioBD', back_populates='emails')