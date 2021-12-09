from config import app, db

from model.Disciplina import Disciplina
from utils.http_utils import create_response, HTTP_OK, HTTP_ERR
from flask import request


@app.route('/disciplina', methods=['get'])
def listar_disciplinas():

    disciplinas = db.session.query(Disciplina).all()
    disciplinas_dict = [disciplina.to_json() for disciplina in disciplinas]
    return create_response(disciplinas_dict, HTTP_OK)


@app.route('/disciplina', methods=['post'])
def criar_disciplina():
    requisicao = request.get_json()

    print(requisicao)

    disciplina = Disciplina(
        nome=requisicao['nome'], carga_horaria=requisicao['carga_horaria'], ementa=requisicao['ementa'])

    resultado = {}
    resultado['status'] = HTTP_OK

    try:
        db.session.add(disciplina)
        db.session.commit()
    except Exception as ex:
        resultado['status'] = HTTP_ERR
        resultado['error'] = str(ex)

    return create_response(resultado, resultado['status'])
