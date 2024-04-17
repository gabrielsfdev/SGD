from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

#Modelo da tabela Email
class EmailBD(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey('usuario.id'))
    email = Column(String(100), unique=True)
    datacadastro_email = Column(DateTime, default=datetime.now())
    usuario = relationship('UsuarioBD', back_populates='emails')