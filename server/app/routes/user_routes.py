from flask import Blueprint, jsonify, request
from ..services.user_services import create_user, get_user

# www.projectw.com/users/....
bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/', methods=['POST'])
def add_user():
    data = request.json
    user = create_user(data)
    return jsonify(user), 201

@bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404