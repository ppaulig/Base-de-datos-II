from bson import ObjectId

def obtener_proveedores(db):

    return list(db.suppliers.find())

def insertar_proveedor(db):

    proveedor = {
        "nombre": "Electro S.A.",
        "contacto": "María Gómez",
        "telefono": "+5491122334455",
        "email": "contacto@electrosa.com",
        "productosOfrecidos": ["PROD101", "PROD102"]
    }

    resultado = db.suppliers.insert_one(proveedor)
    return str(resultado.inserted_id)

def borrar_proveedor(db, proveedor_id):

    proveedor_oid = ObjectId(proveedor_id)

    # Eliminar productos asociados al proveedor
    db.products.delete_many({"proveedorId": proveedor_oid})

    # Eliminar el proveedor
    resultado = db.suppliers.delete_one({"_id": proveedor_oid})

    return resultado.deleted_count > 0
