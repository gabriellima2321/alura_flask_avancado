from db_connection import app,Jogos,db

def add_game(nome,categoria,plataforma):
    auth = Jogos.query.filter_by(nome=nome).first()
    if not auth:
        new_game = Jogos(nome=nome, categoria=categoria, console=plataforma)
        db.session.add(new_game)
        db.session.commit()
        add = Jogos.query.filter_by(nome=nome).first()
        id = add.id
        if add:
            return id
    db.session.rollback()
    return 0

def edita_game(id,nome,categoria,plataforma):
    edit = Jogos.query.filter_by(id=id).first()
    if edit:
        edit.nome = nome
        edit.categoria = categoria
        edit.console = plataforma
        db.session.add(edit)
        db.session.commit()
        return True
    db.session.rollback()
    return False

def delete_game(id):
    delete = Jogos.query.filter_by(id=id).first()
    if delete:
        Jogos.query.filter_by(id=id).delete()
        db.session.commit()
        return True
    db.session.rollback()
    return False
