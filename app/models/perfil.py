from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

#Modelo da tabela Perfil
class PerfilBD(Base):
    __tablename__ = 'perfil'
    id = Column(Integer, primary_key=True)
    nome_perfil = Column(String(50))
    datacadastro_perfil = Column(DateTime, default=datetime.now())
    perfilusuario = relationship('PerfilUsuarioBD', back_populates='perfil')