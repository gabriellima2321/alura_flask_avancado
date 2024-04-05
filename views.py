from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
from authenticator import authenticate,inst_infuser
from db_connection import app,Jogos,session,upload_dir
from games_esp import add_game,edita_game,delete_game

@app.route('/')
def index():  # put application's code here
    #Inicia sessao colocando usuario e senha
    if 'user' not in session:
        session['user'] = ''
        session['password'] = ''

    #autentica usuario conforme a base de dados.
    auth = authenticate(session['user'],session['password'])
    if auth:
        lista_de_jogos = Jogos.query.order_by(Jogos.id)
        return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login(): #Pagina de login
    return render_template('login_form.html')

@app.route('/authenticar', methods=['POST'])
def authenticar():
        auth = authenticate(request.form['username'],request.form['password'])
        if auth:
            session['user'] = request.form['username']
            session['password'] = request.form['password']
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

@app.route('/cadastrar')
def cadastrar():  # put application's code here
    return render_template('cadastra.html')

@app.route('/cadastrar/usuario/nome/senha/email/', methods=['POST'])
def cadastro_usuario():
    user = request.form['user']
    name = request.form['nome']
    email = request.form['email']
    password = request.form['senha']

    cad = inst_infuser(user,name,email,password)
    if cad:
        session['user'] = user
        session['password'] = password
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():  # put application's code here
    session['user'] = None
    session['password'] = None
    return redirect(url_for('login'))

@app.route('/adiciona-jogo')
def novo_jogo():  # put application's code here
    auth = authenticate(session['user'],session['password'])
    if auth:
        return render_template('cadastra_jogo.html',titulo='Novo Jogo')
    else:
        return redirect(url_for('login'))

@app.route('/criar', methods=['POST'])
def criar():  # put application's code here
    nome = request.form['nomeJogo']
    categoria = request.form['categoria']
    plataforma = request.form['plataforma']
    jogo_criado = add_game(nome,categoria,plataforma)
    print(jogo_criado)
    if int(jogo_criado) > 0:

        arquivo = request.files['arquivo']
        arquivo.save(f'{upload_dir}/capa_{jogo_criado}_{nome}.jpg')

        return redirect(url_for('index'))
    else:
        return redirect(url_for('novo_jogo'))

@app.route('/imagem_capa_padrao', methods=['POST','GET'])
def imagem_capa_padrao():
    return send_from_directory(f'{upload_dir}','capa_padrao.jpg')

@app.route('/editar-jogo/<int:id>')
def edit_game(id):  # put application's code here
    auth = authenticate(session['user'],session['password'])
    if auth:
        jogo = Jogos.query.filter_by(id=id).first()
        return render_template('edita_jogo.html',titulo='Editando o Jogo', jogo=jogo)
    else:
        return redirect(url_for('login'))

@app.route('/atualizar_game', methods=['POST'])
def atualizar_game():  # put application's code here
    id = request.form['id']
    nome = request.form['nomeJogo']
    categoria = request.form['categoria']
    plataforma = request.form['plataforma']
    adiciona = edita_game(id,nome,categoria,plataforma)
    if adiciona:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/deletar_jogo/<int:id>')
def deletar_jogo(id):
    auth = authenticate(session['user'],session['password'])
    if auth:
        delete_game(id)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))