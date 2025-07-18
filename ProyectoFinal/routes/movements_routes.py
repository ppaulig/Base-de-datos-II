from flask import Blueprint, request, jsonify
from datetime import datetime
from models import movements, products
from database import connection

movimientos_bp = Blueprint('movimientos', __name__)

@movimientos_bp.route('/', methods=['GET'])
def get_movimientos():

    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')

    try:
        if fecha_inicio and fecha_fin:
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
            
            if fecha_inicio > fecha_fin:
                fecha_inicio, fecha_fin = fecha_fin, fecha_inicio

            fecha_fin = fecha_fin.replace(hour=23, minute=59, second=59)

            movimientos = movements.movimientos_por_fecha(
                connection.client_db, fecha_inicio, fecha_fin)
        else:
            movimientos = movements.listar_movimientos(connection.client_db)

        productos = products.listar_productos(connection.client_db)

        return jsonify({
            "movimientos": movimientos,
            "productos": productos
        }), 200

    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400

@movimientos_bp.route('/agregar', methods=['POST'])
def agregar_movimiento():

    movimiento = request.get_json()

    try:
        movimiento_id = movements.registrar_movimiento(connection.client_db, movimiento)
        return jsonify({
            "message": "Movimiento registrado correctamente",
            "movimiento_id": str(movimiento_id)
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
