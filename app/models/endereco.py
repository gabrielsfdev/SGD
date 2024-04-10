from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela Endereço
class EnderecoBD(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey('usuarios.id'))
    logradouro = Column(String(200))
    numero = Column(String(10))
    complemento = Column(String(20), nullable=True)
    bairro = Column(String(50))
    idcidade = Column(Integer, ForeignKey('cidade.id'))
    cidade = relationship('CidadeBD', back_populates='enderecos')
    usuario = relationship('UsuarioBD', back_populates='enderecos')