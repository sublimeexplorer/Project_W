from ..models.user import User
from .. import db

def create_user(data):
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return user.to_dict()

def get_user(user_id):
    user = User.query.get(user_id)
    return user.to_dict() if user else None