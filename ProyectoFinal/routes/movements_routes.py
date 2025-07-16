from flask import Blueprint, request, jsonify
from bson import ObjectId
from datetime import datetime

from models import movements, product
from database import conn_database

movimientos_bp = Blueprint('movimientos', __name__)

# 🔹 Obtener movimientos, con filtro opcional por fecha
@movimientos_bp.route('/', methods=['GET'])
def get_movimientos():
    """
    Devuelve todos los movimientos, con opción de filtrar por rango de fechas (query params).
    """
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
                conn_database.client_db, fecha_inicio, fecha_fin)
        else:
            movimientos = movements.listar_movimientos(conn_database.client_db)

        productos = product.listar_productos(conn_database.client_db)

        return jsonify({
            "movimientos": movimientos,
            "productos": productos
        }), 200

    except ValueError:
        return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400

# 🔹 Agregar nuevo movimiento
@movimientos_bp.route('/agregar', methods=['POST'])
def agregar_movimiento():
    """
    Recibe un movimiento en formato JSON y lo guarda en la base de datos.
    """
    movimiento = request.get_json()

    try:
        movimiento_id = movements.registar_movimiento(conn_database.client_db, movimiento)
        return jsonify({
            "message": "Movimiento registrado correctamente",
            "movimiento_id": str(movimiento_id)
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
