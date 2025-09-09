import os

database_url_from_env = os.environ.get("DATABASE_URL")


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") 
    # Usamos a variável que acabamos de verificar
    SQLALCHEMY_DATABASE_URI = database_url_from_env
    # Desativa avisos do banco
    SQLALCHEMY_TRACK_MODIFICATIONS = False

