from extensions import db

class Sala(db.Model):
    __tablename__ = 'salas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    predio = db.Column(db.String(100), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(100))
    
    #função para debug
    def __repr__(self):
        return f'<Sala {self.nome}>'