from flask import Blueprint, request, jsonify
from bson import ObjectId
from datetime import datetime

from models import product, suppliers
from database import conn_database

productos_bp = Blueprint('productos', __name__)

# 🔹 Obtener todos los productos y proveedores
@productos_bp.route('/', methods=['GET'])
def get_productos():
    productos = product.listar_productos(conn_database.client_db)
    proveedores = suppliers.obtener_proveedores(conn_database.client_db)

    return jsonify({
        "productos": productos,
        "proveedores": proveedores
    }), 200

# 🔹 Agregar un nuevo producto
@productos_bp.route('/agregar', methods=['POST'])
def agregar_producto():
    data = request.get_json()

    nombre = data.get('nombre')
    codigo = data.get('codigo')
    precio = data.get('precio')
    stock_actual = data.get('stockActual', 0)
    stock_minimo = data.get('stockMinimo', 0)
    categoria = data.get('categoria')
    proveedor_id = data.get('proveedorId')

    if not nombre or precio is None:
        return jsonify({"error": "Nombre y precio son obligatorios"}), 400

    producto = {
        "nombre": nombre,
        "codigo": codigo,
        "precio": float(precio),
        "stockActual": int(stock_actual),
        "stockMinimo": int(stock_minimo),
        "categoria": categoria,
        "proveedorId": ObjectId(proveedor_id) if proveedor_id else None,
        "fechaUltimaActualizacion": datetime.now()
    }

    producto_id = product.agregar_producto(conn_database.client_db, producto)

    return jsonify({
        "message": "Producto agregado correctamente",
        "producto_id": str(producto_id)
    }), 201

# 🔹 Eliminar producto
@productos_bp.route('/eliminar/<producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    success = product.eliminar_producto(conn_database.client_db, producto_id)

    if not success:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({"message": "Producto eliminado"}), 200

# 🔹 Editar producto
@productos_bp.route('/editar/<producto_id>', methods=['PUT'])
def editar_producto(producto_id):
    db = conn_database.client_db
    data = request.get_json()

    producto_actualizado = {
        "nombre": data.get('nombre'),
        "categoria": data.get('categoria'),
        "precio": float(data.get('precio')),
        "stockActual": int(data.get('stockActual')),
        "stockMinimo": int(data.get('stockMinimo')),
        "proveedorId": ObjectId(data.get('proveedorId')) if data.get('proveedorId') else None,
        "fechaUltimaActualizacion": datetime.now()
    }

    product.editar_producto(db, producto_id, producto_actualizado)

    return jsonify({"message": "Producto actualizado"}), 200

# 🔹 Ver stock de productos y productos con stock bajo
@productos_bp.route('/stock', methods=['GET'])
def ver_stock():
    db = conn_database.client_db
    productos_faltantes = product.productos_con_stock_bajo(d
