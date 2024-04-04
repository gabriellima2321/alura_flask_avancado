from flask import Flask, render_template, request, redirect, session, flash, url_for
from games import Game
from authenticator import authenticate
from flask_sqlalchemy import SQLAlchemy
from db_info import DBInfo

app = Flask(__name__)
app.secret_key = 'alura'
dba = DBInfo()
app.config['SQLALCHEMY_DATABASE_URI'] = str(dba)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rcvry@localhost/jogoteca'
db1 = SQLAlchemy()
db1.init_app(app)


class Jogos(db1.Model):
    __tablename__ = 'jogos'
    id = db1.Column(db1.Integer, primary_key=True, autoincrement=True)
    nome = db1.Column(db1.String, nullable=False)
    categoria = db1.Column(db1.String, nullable=False)
    console = db1.Column(db1.String, nullable=False)


usuarios_registrados = [{'nome': 'admin', 'email': 'admin', 'senha': 'admin'}]

def authentica_senha():
    if 'usuario' not in session:
        session['usuario'] = 'alura'
        session['senha_logada'] = 'alura'

    logado = Login.authenticate(session['usuario'], session['senha_logada'])
    print(logado)
    return logado


@app.route('/adiciona-jogo')
def novo_jogo():  # put application's code here
    if authentica_senha():
        return render_template('cadastra_jogo.html',titulo='Novo Jogo')
    else:
        return redirect(url_for('login'))

@app.route('/criar', methods=['POST'])
def criar():  # put application's code here
    nome = request.form['nomeJogo']
    categoria = request.form['categoria']
    plataforma = request.form['plataforma']
    jogo_criado = Game(nome,categoria,plataforma)
    #lista_de_jogos.append(jogo_criado)
    return redirect(url_for('index'))


@app.route('/login')
def login():  # put application's code here
    return render_template('login_form.html')

@app.route('/authenticar', methods=['POST'])
def authenticar():
        logado = authentica(request.form['username'],request.form['password'])
        if logado:
            session['usuario'] = request.form['username']
            session['senha_logada'] = request.form['password']
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

@app.route('/cadastrar')
def cadastrar():  # put application's code here
    return render_template('cadastra.html')

@app.route('/cadastrar/usuario/nome/senha/email/??/', methods=['POST'])
def cadastro_usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    #usuario = Usuario(nome, email, senha)
    session['usuario'] = usuario._usuario
    session['senha_logada'] = usuario._senha
    novo_usuario = {'nome': usuario._usuario, 'email': usuario._email, 'senha': usuario._senha}
    usuarios_registrados.append(novo_usuario)
    return redirect(url_for('index'))


@app.route('/logout')
def logout():  # put application's code here
    session['usuario'] = None
    session['senha_logada'] = None
    return redirect(url_for('login'))

@app.route('/')
def index():  # put application's code here
    if 'usuario' not in session:
        session['usuario'] = 'alura'
        session['senha_logada'] = 'alura'

    print(app.config['SQLALCHEMY_DATABASE_URI'])
    print(db1.Model)
    logado = authenticate('alura','alura')
    #print(lista)

    auth = True
    if auth:
        lista_de_jogos = Jogos.query.order_by(Jogos.id)
        return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

