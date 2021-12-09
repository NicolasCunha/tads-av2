from config import app, db

from model.Pessoa import Pessoa
from utils.http_utils import create_response, HTTP_OK, HTTP_ERR
from flask import request


@app.route('/pessoa', methods=['get'])
def listar_pessoas():

    pessoas = db.session.query(Pessoa).all()
    pessoas_dict = [pessoa.to_json() for pessoa in pessoas]

    return create_response(pessoas_dict, HTTP_OK)


@app.route('/pessoa', methods=['post'])
def criar_pessoa():
    requisicao = request.get_json()

    pessoa = Pessoa(nome=requisicao['nome'], cpf=requisicao['cpf'], email=requisicao['email'])
    resultado = {}
    resultado['status'] = HTTP_OK

    try:
        db.session.add(pessoa)
        db.session.commit()
    except Exception as ex:
        resultado['status'] = HTTP_ERR
        resultado['error'] = str(ex)

    return create_response(resultado, resultado['status'])
