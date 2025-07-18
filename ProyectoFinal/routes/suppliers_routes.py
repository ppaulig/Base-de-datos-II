from flask import Blueprint, request, jsonify
from models import suppliers
from database import connection

proveedores_bp = Blueprint('proveedores', __name__)

@proveedores_bp.route('/', methods=['GET'])
def get_proveedores():
    proveedores = suppliers.obtener_proveedores(connection.client_db)
    return jsonify(proveedores), 200

@proveedores_bp.route('/agregar', methods=['POST'])
def agregar_proveedor():
    data = request.get_json()

    nombre = data.get('nombre')
    telefono = data.get('telefono')
    email = data.get('email')
    contacto = data.get('contacto')
    
    if not nombre or not telefono or not email:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400
    
    proveedor = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "contacto": contacto
    }
    
    proveedor_id = suppliers.insertar_proveedor(connection.client_db, proveedor)

    return jsonify({
        "message": "Proveedor agregado correctamente",
        "proveedor_id": str(proveedor_id)
    }), 201
    
@proveedores_bp.route('/eliminar/<proveedor_id>', methods=['POST'])
def eliminar_proveedor(proveedor_id):
    if not suppliers.borrar_proveedor(connection.client_db, proveedor_id):
        return jsonify({"error": "Proveedor no encontrado"}), 404
    
    return jsonify({"message": "Proveedor eliminado"}), 200
