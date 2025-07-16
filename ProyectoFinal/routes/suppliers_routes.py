from flask import Blueprint, request, jsonify, redirect, url_for, render_template

from models import suppliers
from database import conn_database

proveedores_bp = Blueprint('proveedores', __name__)

@proveedores_bp.route('/', methods=['GET'])
def get_proveedores():
    proveedores = suppliers.obtener_proveedores(conn_database.client_db)
    return render_template('proveedores.html', proveedores=proveedores)

@proveedores_bp.route('/agregar', methods=['POST'])
def agregar_proveedor():
    """
    Procesa el formulario para agregar un nuevo proveedor.

    Redirige a la lista de proveedores o retorna error.
    """
    nombre = request.form.get('nombre')
    telefono = request.form.get('telefono')
    email = request.form.get('email')
    contacto = request.form.get('contacto')
    
    if not nombre or not telefono or not email:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400
    
    proveedor = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "contacto": contacto
    }
    
    proveedor_id = suppliers.insertar_proveedor(conn_database.client_db, proveedor)
    from flask import Blueprint, request, jsonify
from models import suppliers
from database import conn_database

proveedores_bp = Blueprint('proveedores', __name__)

# 🔹 Obtener todos los proveedores
@proveedores_bp.route('/', methods=['GET'])
def get_proveedores():
    proveedores = suppliers.obtener_proveedores(conn_database.client_db)
    return jsonify({
        "proveedores": proveedores
    }), 200

# 🔹 Agregar un nuevo proveedor
@proveedores_bp.route('/agregar', methods=['POST'])
def agregar_proveedor():
    """
    Agrega un nuevo proveedor a la base de datos.
    Espera JSON en el cuerpo de la petición.
    """
    data = request.get_json()

    nombre = data.get('nombre')
    telefono = data.get('telefono')
    email = data.get('email')
    contacto = data.get('contacto')

    if not nombre or not telefono or not email:
        return jsonify({"error": "Nombre, teléfono y email son obligatorios"}), 400

    proveedor = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "contacto": contacto
    }

    proveedor_id = suppliers.insertar_proveedor(conn_database.client_db, proveedor)

    return jsonify({
        "message": "Proveedor agregado correctamente",
        "proveedor_id": str(proveedor_id)
    }), 201

# 🔹 Eliminar proveedor
@proveedores_bp.route('/eliminar/<proveedor_id>', methods=['DELETE'])
def eliminar_proveedor(proveedor_id):
    success = suppliers.borrar_proveedor(conn_database.client_db, proveedor_id)

    if not success:
        return jsonify({"error": "Proveedor no encontrado"}), 404

    return jsonify({"message": "Proveedor eliminado"}), 200

    return redirect(url_for('proveedores.get_proveedores'))

@proveedores_bp.route('/eliminar/<proveedor_id>', methods=['POST'])
def eliminar_proveedor(proveedor_id):
    if not suppliers.borrar_proveedor(conn_database.client_db, proveedor_id):
        return jsonify({"error": "Proveedor no encontrado"}), 404
    
    return redirect(url_for('proveedores.get_proveedores'))



