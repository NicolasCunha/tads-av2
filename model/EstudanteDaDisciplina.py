from sqlalchemy.sql.schema import ForeignKey
from config import db

from sqlalchemy import ForeignKey

class EstudanteDaDisciplina(db.Model):
    __tablename__ = 'Estudante'
    id_pessoa = db.Column(db.Integer, ForeignKey(
        'Pessoa.id'), primary_key=True)
    id_disciplina = db.Column(db.Integer, ForeignKey(
        'Disciplina.id', primary_key=True))
    semestre = db.Column(db.Integer)
    media_final = db.Column(db.Float)
    frequencia = db.Column(db.Float)

    def to_json(self):
        return {
            'id_pessoa': self.id_pessoa,
            'id_disciplina': self.id_disciplina,
            'semestre': self.semestre,
            'media_final': self.media_final,
            'frequencia': self.frequencia
        }
