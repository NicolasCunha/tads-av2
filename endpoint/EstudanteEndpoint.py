from config import app, db

from model.EstudanteDaDisciplina import EstudanteDaDisciplina
from utils.http_utils import create_response, HTTP_OK, HTTP_ERR
from flask import request


@app.route('/estudante', methods=['get'])
def listar_estudantes():

    estudantes = db.session.query(EstudanteDaDisciplina).all()
    estudantes_dict = [estudante.to_json() for estudante in estudantes]

    return create_response(estudantes_dict, HTTP_OK)


@app.route('/estudante', methods=['post'])
def criar_estudante():
    requisicao = request.get_json()

    estudante = EstudanteDaDisciplina(id_pessoa=requisicao['id_pessoa'], id_disciplina=requisicao['id_disciplina'],
                                      semestre=requisicao['semestre'], media_final=requisicao['media_final'], frequencia=requisicao['frequencia'])
    resultado = {}
    resultado['status'] = HTTP_OK

    try:
        db.session.add(estudante)
        db.session.commit()
    except Exception as ex:
        resultado['status'] = HTTP_ERR
        resultado['error'] = str(ex)

    return create_response(resultado, resultado['status'])
