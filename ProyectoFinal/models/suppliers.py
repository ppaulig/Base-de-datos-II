from bson import ObjectId
from datetime import datetime

def obtener_proveedores(db):
    """
    Obtiene todos los proveedores de la base de datos.

    Args:
        db: Conexión a la base de datos.

    Returns:
        list: Lista de proveedores.
    """
    return list(db.proveedores.find())

def insertar_proveedor(db):
    """
    Inserta un nuevo proveedor de ejemplo en la base de datos.

    Args:
        db: Conexión a la base de datos.

    Returns:
        str: ID del proveedor insertado.
    """
    proveedor = {
        "nombre": "Electro S.A.",
        "contacto": "María Gómez",
        "telefono": "+5491122334455",
        "email": "contacto@electrosa.com",
        "productosOfrecidos": ["PROD101", "PROD102"]
    }

    resultado = db.proveedores.insert_one(proveedor)
    return str(resultado.inserted_id)

def borrar_proveedor(db, proveedor_id):
    """
    Elimina un proveedor de la base de datos y los productos asociados.

    Args:
        db: Conexión a la base de datos.
        proveedor_id: ID del proveedor a eliminar.

    Returns:
        bool: True si se eliminó correctamente, False en caso contrario.
    """
    proveedor_oid = ObjectId(proveedor_id)

    # Eliminar productos asociados al proveedor
    db.productos.delete_many({"proveedorId": proveedor_oid})

    # Eliminar el proveedor
    resultado = db.proveedores.delete_one({"_id": proveedor_oid})

    return resultado.deleted_count > 0
