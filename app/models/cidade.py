from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela Cidade
class CidadeBD(Base):
    __tablename__ = 'cidade'
    id = Column(Integer, primary_key=True)
    nomecidade = Column(String(100))
    uf = Column(String(2))
    enderecos = relationship('EnderecoBD', back_populates='cidade')