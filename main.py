import os
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path=dotenv_path)

# Importa as configurações e extensões
from config import Config
from extensions import db
from views.database_view import salas_bp
from views.general_views import general_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa o banco de dados com a aplicação
    db.init_app(app)
    
    # Incializa o migrate do banco de dados
    migrate = Migrate(app, db)

    # Registra os Blueprints (conjuntos de rotas)
    app.register_blueprint(salas_bp)
    app.register_blueprint(general_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

