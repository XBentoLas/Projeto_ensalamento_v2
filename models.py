from extensions import db

# Tabelas de associação

professor_areas_association = db.Table('professor_areas',
    db.Column('professor_id', db.Integer, db.ForeignKey('professores.id'), primary_key=True),
    db.Column('area_id', db.Integer, db.ForeignKey('areas_de_atuacao.id'), primary_key=True)
)

disciplina_areas_association = db.Table('disciplina_areas',
    db.Column('disciplina_id', db.Integer, db.ForeignKey('disciplinas.id'), primary_key=True),
    db.Column('area_id', db.Integer, db.ForeignKey('areas_de_atuacao.id'), primary_key=True)
)


# Tabelas princiapais

class Sala(db.Model):
    __tablename__ = 'salas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=True)
    predio = db.Column(db.String(50), nullable=True)
    capacidade = db.Column(db.Integer, nullable=True)
    tipo = db.Column(db.String(50), nullable=True)

    disponibilidades = db.relationship('Disponibilidade', back_populates='sala', cascade="all, delete-orphan")
    ocupacoes = db.relationship('Ocupacao', back_populates='sala', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Sala {self.nome} - {self.predio}>'


class Professor(db.Model):
    __tablename__ = 'professores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)

    disponibilidade = db.relationship('DisponibilidadeProfessor', back_populates='professor', uselist=False, cascade="all, delete-orphan")
    areas = db.relationship('AreaDeAtuacao', secondary=professor_areas_association, back_populates='professores')
    turmas = db.relationship('Turma', back_populates='professor')

    def __repr__(self):
        return f'<Professor {self.nome}>'


class AreaDeAtuacao(db.Model):
    __tablename__ = 'areas_de_atuacao'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)

    professores = db.relationship('Professor', secondary=professor_areas_association, back_populates='areas')
    disciplinas = db.relationship('Disciplina', secondary=disciplina_areas_association, back_populates='areas')

    def __repr__(self):
        return f'<AreaDeAtuacao {self.nome}>'


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    codigo = db.Column(db.String(50), nullable=True)

    areas = db.relationship('AreaDeAtuacao', secondary=disciplina_areas_association, back_populates='disciplinas')
    turmas = db.relationship('Turma', back_populates='disciplina')

    def __repr__(self):
        return f'<Disciplina {self.codigo}>'


class Disponibilidade(db.Model):
    __tablename__ = 'disponibilidades'

    id = db.Column(db.Integer, primary_key=True)
    dia_semana = db.Column(db.Enum('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=True)
    hora_fim = db.Column(db.Time, nullable=True)

    sala_id = db.Column(db.Integer, db.ForeignKey('salas.id'), nullable=True)
    sala = db.relationship('Sala', back_populates='disponibilidades')

    def __repr__(self):
        return f'<Disponibilidade Sala {self.sala_id} - {self.dia_semana}>'


class Ocupacao(db.Model):
    __tablename__ = 'ocupacoes'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=True)
    hora_inicio = db.Column(db.Time, nullable=True)
    hora_fim = db.Column(db.Time, nullable=True)
    descricao = db.Column(db.String(255), nullable=True)

    sala_id = db.Column(db.Integer, db.ForeignKey('salas.id'), nullable=True)
    sala = db.relationship('Sala', back_populates='ocupacoes')

    def __repr__(self):
        return f'<Ocupacao Sala {self.sala_id} - {self.data}>'


class DisponibilidadeProfessor(db.Model):
    __tablename__ = 'disponibilidade_professores'

    id = db.Column(db.Integer, db.ForeignKey('professores.id'), primary_key=True)
    dia_semana = db.Column(db.Enum('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'), nullable=True)
    hora_inicio = db.Column(db.Time, nullable=True)
    hora_fim = db.Column(db.Time, nullable=True)

    professor = db.relationship('Professor', back_populates='disponibilidade')

    def __repr__(self):
        return f'<Disponibilidade Professor {self.id}>'


class Turma(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    periodo = db.Column(db.Enum('Matutino', 'Vespertino', 'Noturno'), nullable=True)
    num_alunos = db.Column(db.Integer, nullable=True)

    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)

    professor = db.relationship('Professor', back_populates='turmas')
    disciplina = db.relationship('Disciplina', back_populates='turmas')
    
    def __repr__(self):
        return f'<Turma {self.nome}>'

