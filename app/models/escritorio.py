from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

#Modelo da tabela Escritorio
class EscritorioBD(Base):
    __tablename__ = 'escritorio'
    id = Column(Integer, primary_key=True)
    escritorio = Column(String(50))
    escritoriopai = Column(Integer, ForeignKey('escritorio.id'))
    escritorio = relationship('EscritorioBD', back_populates='escritorio')
    arquivo = relationship('ArquivoBD', back_populates='arquivo')