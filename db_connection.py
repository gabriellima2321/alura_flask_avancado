import os.path
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from db_info import DBInfo

# Inicialize o Flask
app = Flask(__name__)

# Configuração do SQLAlchemy para a primeira instância
app.secret_key = 'alura'
dba = DBInfo()
app.config['SQLALCHEMY_DATABASE_URI'] = str(dba)
db = SQLAlchemy(app)
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '\\uploads'
upload_dir = app.config['UPLOAD_PATH'] = UPLOAD_PATH

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    usuario = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    senha = db.Column(db.String(100), nullable=False)

class Jogos(db.Model):
    __tablename__ = 'jogos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String, nullable=False)
    console = db.Column(db.String, nullable=False)