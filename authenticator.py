from db_connection import app,Usuarios,db

def authenticate(user, password):
    auth = Usuarios.query.filter_by(usuario=user, senha=password).first()
    if auth:
        return True
    else:
        return False

def inst_infuser(user, nome, email, password):
    auth = Usuarios.query.filter_by(usuario=user).first()
    if not auth:
        new_user = Usuarios(usuario=user, nome=nome, email=email, senha=password)
        db.session.add(new_user)
        add = Usuarios.query.filter_by(usuario=user).first()
        db.session.commit()
        if add:
            return True

    db.session.rollback()
    return False