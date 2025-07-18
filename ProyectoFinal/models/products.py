from bson import ObjectId

def listar_productos(db):

    pipeline = [
        {
            "$lookup": {
                "from": "suppliers",
                "localField": "proveedorId",
                "foreignField": "_id",
                "as": "proveedor"
            }
        },
        {
            "$unwind": {
                "path": "$proveedor",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$addFields": {
                "nombreProveedor": "$proveedor.nombre"
            }
        },
        {
            "$project": {
                "proveedor": 0
            }
        }
    ]
    return list(db.products.aggregate(pipeline))


def agregar_producto(db, nuevo_producto):

    resultado = db.products.insert_one(nuevo_producto)
    return str(resultado.inserted_id)


def eliminar_producto(db, producto_id):

    resultado = db.products.delete_one({"_id": ObjectId(producto_id)})
    return resultado.deleted_count > 0


def editar_producto(db, producto_id, datos_actualizados):

    resultado = db.products.update_one(
        {"_id": ObjectId(producto_id)},
        {"$set": datos_actualizados}
    )
    return resultado.modified_count > 0


def actualizar_stock(db, producto_id, diferencia_stock):

    producto = db.products.find_one({"_id": ObjectId(producto_id)})

    if producto:
        stock_actual = producto.get("stockActual", 0)
        nuevo_valor = int(stock_actual) + int(diferencia_stock)

        if nuevo_valor < 0:
            return False

        resultado = db.products.update_one(
            {"_id": ObjectId(producto_id)},
            {"$set": {"stockActual": nuevo_valor}}
        )
        return resultado.modified_count > 0

    return False


def consultar_stock_producto(db, producto_id):

    producto = db.products.find_one(
        {"_id": ObjectId(producto_id)},
        {"_id": 1, "nombre": 1, "stockActual": 1, "stockMinimo": 1}
    )

    if producto:
        return {
            "_id": str(producto["_id"]),
            "nombre": producto.get("nombre"),
            "stockActual": producto.get("stockActual", 0),
            "stockMinimo": producto.get("stockMinimo", 0)
        }


def productos_con_stock_bajo(db):

    pipeline = [
        {
            "$match": {
                "$expr": {
                    "$lt": ["$stockActual", "$stockMinimo"]
                }
            }
        },
        {
            "$lookup": {
                "from": "suppliers",
                "localField": "proveedorId",
                "foreignField": "_id",
                "as": "proveedor"
            }
        },
        {
            "$unwind": {
                "path": "$proveedor",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$addFields": {
                "nombreProveedor": "$proveedor.nombre"
            }
        },
        {
            "$project": {
                "proveedor": 0
            }
        }
    ]
    return list(db.products.aggregate(pipeline))
