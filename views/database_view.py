from flask import Blueprint, render_template
from models import Sala 

# A variável que o main.py está procurando é definida aqui.
salas_bp = Blueprint('salas', __name__)

@salas_bp.route('/salas')
def mostrar_salas():
    try:
        todas_as_salas = Sala.query.all()
    except Exception as e:
        todas_as_salas = []
        print(f"Erro ao acessar o banco de dados: {e}")

    return render_template('db_viewer.html', salas=todas_as_salas)

