from flask import Blueprint, jsonify

# www.projectw.com/
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({"message": "Hello Project W"})