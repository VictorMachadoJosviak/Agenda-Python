"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request,jsonify
from AgendaContatos import app
import AgendaContatos.Database as db


@app.route('/')
@app.route('/home')
def home():
  
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,)

@app.route('/')
@app.route('/contato')
def contato():
   
    return render_template('editContato.html',
        title='contato Page',
        year=datetime.now().year,)


#WEB APIS

@app.route('/api/deletePessoa', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def deletePessoa():
    content = request.json
    if request.method == 'POST':
        db.excluirPessoa(content["id"])
        return "Pessoa excluida com sucesso",200    


@app.route('/api/buscaPessoaPorId/<id>', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def buscaPessoaPorId(id=None):
    if request.method == 'GET':
        pessoa = db.buscaPessoaPorId(id)
        json = {
            "id" : pessoa.id,
            "nome" : pessoa.nome,
            "email" : pessoa.email
            }
        return jsonify(json),200


@app.route('/api/edit', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def edit():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        content = request.json
        if isNullOrEmpty(content["id"]):            
            pessoaId = db.insertPessoa(content["nome"],content["email"])
            json = {
                "id" : pessoaId
                }          
            return jsonify(json),200
        else:           
            db.atualizaPessoa(content["id"],content["nome"],content["email"])
            print("pessoa atualizada")
       
        return "pessoa salva com sucesso",200

@app.route('/api/list', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def list():
    if request.method == 'GET': 
        lista = db.listarContatos()
        array = []
        for x in lista:
            array.append({
                    "id" : x.id,
                    "nome" : x.nome,
                    "email":x.email
                })
        return jsonify(array),200
  
@app.route('/api/salvarTelefone', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def salvarTelefone():
    if request.method == 'POST':
        content = request.json    
        if isNullOrEmpty(content["id"]):
            print("cadastrado novo")
            db.inserirTelefone(content["numero"],content["pessoaId"])
        else:
             print("telefone atualizado")
             db.atualizaTelefone(content["id"],content["numero"],content["pessoaId"])

        return "telefone salvo",200

@app.route('/api/saveEndereco', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def saveEndereco():
    if request.method == 'POST':
        content = request.json   
        if isNullOrEmpty(content["id"]):            
           db.cadastrarEndereco(content["rua"],content["numero"],content["cep"],content["pessoaId"])
        else:
            print("Endereco atualizado")
            db.atualizaEndereco(content["id"],content["rua"],content["numero"],content["cep"],content["pessoaId"])
        return "endereco salvo",200

@app.route('/api/deleteEndereco', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def deleteEndereco():
    if request.method == 'POST':
        content = request.json
        db.excluirEndereco(content["pessoaId"],content["enderecoId"])
        return "endereco excluido com sucesso",200


@app.route('/api/deleteTelefone', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def deleteTelefone():
    if request.method == 'POST':
        content = request.json      
        db.excluirTelefone(content["pessoaId"],content["telefoneId"])
        return "telefone excluido com sucesso",200

@app.route('/api/getListPhoneByUserId/<pessoaId>', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def getListPhoneByUserId(pessoaId=None):
    if request.method == 'GET':   
        telefones = db.pesquisaTelefonePorPessaId(pessoaId)
        array = []
        for x in telefones:
            array.append({
                "id" : x.id,
                "numero" : x.numero
                })
        return jsonify(array),200

@app.route('/api/getListAddressByUserId/<pessoaId>', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def getListAddressByUserId(pessoaId=None):
    if request.method == 'GET':   
        telefones = db.pesquisaEnderecoPorPessaId(pessoaId)
        array = []
        for x in telefones:
            array.append({
                "id" : x.id,
                "numero" : x.numero,
                "rua" : x.rua,
                "cep" : x.cep
                })
        return jsonify(array),200


def isNullOrEmpty(item):
    if item == None or item == "":
        return True
    else:
        return False