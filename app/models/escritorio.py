from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime

#Modelo da tabela Escritorio
class EscritorioBD(Base):
    __tablename__ = 'escritorio'
    id = Column(Integer, primary_key=True)
    nome_escritorio = Column(String(50))
    escritoriopai = Column(Integer, ForeignKey('escritorio.id'))
    datacadastro_escritorio = Column(DateTime, default=datetime.now())
    sub_escritorios = relationship('EscritorioBD', back_populates='escritorio_pai', remote_side=[id])  # Lista de sub-escritórios
    escritorio_pai = relationship('EscritorioBD', back_populates='sub_escritorios', remote_side=[escritoriopai])  # Escritório pai
    arquivos = relationship('ArquivoBD', back_populates='escritorio')
    arquivoescritorio = relationship('ArquivoEscritorioBD', back_populates='escritorio')
    escritoriousuario = relationship('EscritorioUsuarioBD', back_populates='escritorio')