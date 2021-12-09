from config import db

class Disciplina(db.Model):
    __tablename__ = 'Disciplina'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(254))
    carga_horaria = db.Column(db.Integer)
    ementa = db.Column(db.String(254))

    def to_json(self):
        return {
            'id' : self.id,
            'nome' : self.nome,
            'carga_horaria' : self.carga_horaria,
            'ementa' : self.ementa
        }