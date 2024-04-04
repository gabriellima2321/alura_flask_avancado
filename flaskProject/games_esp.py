from db_connection import app,Jogos,db

def add_game(nome,categoria,plataforma):
    auth = Jogos.query.filter_by(nome=nome).first()
    if not auth:
        new_game = Jogos(nome=nome, categoria=categoria, console=plataforma)
        db.session.add(new_game)
        db.session.commit()
        add = Jogos.query.filter_by(nome=nome).first()
        if add:
            return True
    db.session.rollback()
    return False