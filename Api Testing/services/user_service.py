from main import db
from models import User


def create_user(name):
    user = User(userName=name)
    db.session.add(user)
    db.session.commit()
    return user