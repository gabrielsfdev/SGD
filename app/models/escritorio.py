from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela Escritorio
class EscritorioBD(Base):
    __tablename__ = 'escritorio'
    id = Column(Integer, primary_key=True)
    nome_escritorio = Column(String(50))
    escritoriopai = Column(Integer, ForeignKey('escritorio.id'))
    sub_escritorios = relationship('EscritorioBD', back_populates='escritorio_pai', remote_side=[id])  # Lista de sub-escritórios
    escritorio_pai = relationship('EscritorioBD', back_populates='sub_escritorios', remote_side=[escritoriopai])  # Escritório pai
    arquivos = relationship('ArquivoBD', back_populates='escritorio')