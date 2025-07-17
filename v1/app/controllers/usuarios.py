from flask import Blueprint, request, jsonify

usuarios_endpoints = Blueprint('usuarios_endpoints', __name__)

@usuarios_endpoints.route('/saludo', methods=['GET'])
def saludo_usuario():
    user_id = request.args.get('id')
    if user_id:
        mensaje = f"El id del usuario es {user_id}"
    else:
        mensaje = "Lista de todos los usuarios."
    return jsonify({"mensaje": mensaje}), 200
