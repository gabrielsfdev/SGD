from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

#Modelo da tabela Telefone
class TelefoneBD(Base):
    __tablename__ = 'telefone'
    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey('usuario.id'))
    numero_telefone = Column(String(14), unique=True)
    datacadastro_telefone = Column(DateTime, default=datetime.now())
    usuario = relationship('UsuarioBD', back_populates='telefones')