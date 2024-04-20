from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

#Modelo da tabela Arquivo
class ArquivoBD(Base):
    __tablename__ = 'arquivo'
    id = Column(Integer, primary_key=True)
    nome_arquivo = Column(String(100))
    idusuario = Column(Integer, ForeignKey('usuario.id'))
    idsetor = Column(Integer, ForeignKey('setor.id'), nullable=True)
    idescritorio = Column(Integer, ForeignKey('escritorio.id'), nullable=True)
    datacriacao = Column(DateTime, default=datetime.now())
    restricao = Column(Boolean, default=False)
    tipo_arquivo = Column(String(10))
    tamanho_arquivo = Column(Integer)
    usuario = relationship('UsuarioBD', back_populates='arquivos')
    setor = relationship('SetorBD', back_populates='arquivos')
    escritorio = relationship('EscritorioBD', back_populates='arquivos')
    blob = relationship('ArquivoBlobBD', back_populates='arquivo', uselist=False)
    arquivoescritorio = relationship('ArquivoEscritorioBD', back_populates='arquivo')
    arquivosetor = relationship('ArquivoSetorBD', back_populates='arquivo')
    arquivousuario = relationship('ArquivoUsuarioBD', back_populates='arquivo')
    dadosarquivo = relationship('DadosArquivoBD', back_populates='arquivo')
    dadosdocumento = relationship('DadosDocumentoBD', back_populates='arquivo')