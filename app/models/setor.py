from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela Setor
class SetorBD(Base):
    __tablename__ = 'setor'
    id = Column(Integer, primary_key=True)
    setor = Column(String(50))
    arquivo = relationship('ArquivoBD', back_populates='arquivo')