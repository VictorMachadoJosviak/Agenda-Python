import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Pessoa(Base):
     __tablename__ = 'pessoa'
     id = Column(Integer, primary_key=True)
     nome = Column(String(250), nullable=False)
     email = Column(String(200), nullable = False)
     
     

class Endereco(Base):
     __tablename__ = 'endereco'
     id = Column(Integer, primary_key=True)
     rua = Column(String(250))
     numero = Column(String(250))
     cep = Column(String(250), nullable=False)
     pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
     pessoa = relationship(Pessoa,lazy='joined')

class Telefone(Base):
    __tablename__ = 'telefone'
    id = Column(Integer, primary_key=True)
    numero = Column(String(20))
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship(Pessoa,lazy='joined')

engine = create_engine('sqlite:///AgendaContatosDB.db')
Base.metadata.create_all(engine)