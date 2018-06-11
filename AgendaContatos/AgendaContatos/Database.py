from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from AgendaContatos.DBClasses_sqlite import Endereco, Base, Pessoa, engine,Telefone

DBSession = sessionmaker(bind=engine)

def insertPessoa(nome_,email):
    session = DBSession()
    p = Pessoa(nome=nome_,email=email)
    session.add(p)
    session.commit()  
    return p.id

def buscaPessoaPorId(id):
     session = DBSession()
     pessoa = session.query(Pessoa).filter(Pessoa.id == id).first()   
     session.close()
     return pessoa

def listarContatos():
     session = DBSession()
     pessoas = session.query(Pessoa).all()   
     session.close()
     return pessoas

def cadastrarEndereco(rua,numero,cep,pessoaId):
    session = DBSession()
    p = Endereco(rua=rua,numero=numero,cep=cep,pessoa_id=pessoaId)
    session.add(p)
    session.commit()

def inserirTelefone(numero,pessoa):
    session = DBSession()
    t = Telefone(numero= numero,pessoa_id=pessoa)
    session.add(t)
    session.commit()

def atualizaTelefone(id,numero,pessoa):
    session = DBSession()
    tel = session.query(Telefone).filter(Telefone.id == id and Telefone.pessoa_id == pessoa).update({
          "numero" : (numero)          
        })   
    session.commit()
    session.close()

def atualizaPessoa(id,nome,email):
    session = DBSession()
    tel = session.query(Pessoa).filter(Pessoa.id == id).update({
          "nome" : (nome),
          "email" : (email)
        })   
    session.commit()
    session.close()

def atualizaEndereco(id,rua,numero,cep,pessoaId):
    session = DBSession()
    tel = session.query(Endereco).filter(Endereco.id == id and Endereco.pessoa_id == pessoa).update({
          "numero" : (numero),
          "cep" : (cep),
          "rua" : (rua)
        })   
    session.commit()
    session.close()

def pesquisaTelefonePorPessaId(idPessoa):
    session = DBSession() 
    pessoa = session.query(Telefone).filter(Telefone.pessoa_id == idPessoa).all()
    return pessoa

def pesquisaEnderecoPorPessaId(idPessoa):
    session = DBSession() 
    pessoa = session.query(Endereco).filter(Endereco.pessoa_id == idPessoa).all()
    return pessoa

def excluirTelefone(idPessoa,idTelefone):
     session = DBSession();
     telefone = session.query(Telefone).filter(Telefone.pessoa_id == idPessoa and Telefone.id == idTelefone).first()
     session.delete(telefone)
     session.commit()
     session.close()

def excluirPessoa(idPessoa):
     session = DBSession();
     pessoa = session.query(Pessoa).filter(Pessoa.id == idPessoa).first()
     session.delete(pessoa)
     session.commit()
     session.close()

def excluirEndereco(idPessoa,idEndereco):
     session = DBSession();
     endereco = session.query(Endereco).filter(Endereco.pessoa_id == idPessoa and Endereco.id == idEndereco).first()
     session.delete(endereco)
     session.commit()
     session.close()



    
def isNullOrEmpty(item):
    if item == None or item == "":
        return True
    else:
        return False
    
