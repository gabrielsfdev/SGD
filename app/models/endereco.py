from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

#Modelo da tabela Endereço
class EnderecoBD(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key=True)
    idusuario = Column(Integer, ForeignKey('usuario.id'))
    cep = Column(String(9))
    logradouro = Column(String(200))
    numero = Column(String(10))
    complemento = Column(String(20), nullable=True)
    bairro = Column(String(50))
    idcidade = Column(Integer, ForeignKey('cidade.id'))
    datacadastro_endereco = Column(DateTime, default=datetime.now())
    cidade = relationship('CidadeBD', back_populates='enderecos')
    usuario = relationship('UsuarioBD', back_populates='enderecos')