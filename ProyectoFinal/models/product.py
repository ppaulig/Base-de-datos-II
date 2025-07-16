from bson import ObjectId

def listar_productos(db):
    """
    Recupera todos los productos junto con el nombre de su proveedor asociado.

    Args:
        db: Instancia de conexión a la base de datos.

    Returns:
        list: Lista de productos con el campo 'proveedorNombre' añadido.
    """
    pipeline = [
        {
            "$lookup": {
                "from": "proveedores",
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
    return list(db.productos.aggregate(pipeline))


def agregar_producto(db, nuevo_producto):
    """
    Registra un nuevo producto en la base de datos.

    Args:
        db: Objeto de conexión MongoDB.
        nuevo_producto (dict): Datos del producto a insertar.

    Returns:
        str: ID del producto recién insertado.
    """
    resultado = db.productos.insert_one(nuevo_producto)
    return str(resultado.inserted_id)


def eliminar_producto(db, producto_id):
    """
    Elimina un producto según su ID.

    Args:
        db: Base de datos MongoDB.
        producto_id: Identificador del producto a borrar.

    Returns:
        bool: True si se eliminó exitosamente.
    """
    resultado = db.productos.delete_one({"_id": ObjectId(producto_id)})
    return resultado.deleted_count > 0


def editar_producto(db, producto_id, datos_actualizados):
    """
    Actualiza los campos de un producto específico.

    Args:
        db: Conexión a la base.
        producto_id: ID del producto.
        datos_actualizados: Campos nuevos a establecer.

    Returns:
        bool: True si hubo modificación.
    """
    resultado = db.productos.update_one(
        {"_id": ObjectId(producto_id)},
        {"$set": datos_actualizados}
    )
    return resultado.modified_count > 0


def actualizar_stock(db, producto_id, diferencia_stock):
    """
    Suma o resta unidades al stock actual del producto.

    Args:
        db: Conexión a MongoDB.
        producto_id: ID del producto.
        diferencia_stock: Valor entero a modificar (positivo o negativo).

    Returns:
        bool: True si el stock fue modificado correctamente.
    """
    producto = db.productos.find_one({"_id": ObjectId(producto_id)})

    if producto:
        stock_actual = producto.get("stockActual", 0)
        nuevo_valor = int(stock_actual) + int(diferencia_stock)

        if nuevo_valor < 0:
            return False

        resultado = db.productos.update_one(
            {"_id": ObjectId(producto_id)},
            {"$set": {"stockActual": nuevo_valor}}
        )
        return resultado.modified_count > 0

    return False


def consultar_stock_producto(db, producto_id):
    """
    Consulta el stock actual y mínimo de un producto dado.

    Args:
        db: Instancia de la base de datos.
        producto_id: Identificador del producto.

    Returns:
        dict: Información básica del producto y su stock.
    """
    producto = db.productos.find_one(
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
    """
    Devuelve los productos cuyo stock actual es inferior al mínimo establecido.

    Args:
        db: Conexión con la base MongoDB.

    Returns:
        list: Lista de productos con bajo stock, incluyendo el nombre del proveedor.
    """
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
                "from": "proveedores",
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
    return list(db.productos.aggregate(pipeline))
