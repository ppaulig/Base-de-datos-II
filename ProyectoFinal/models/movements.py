from bson import ObjectId
from datetime import datetime

from models import model_producto

def listar_movimientos(db):
    """
    Recupera todos los registros de movimientos, incorporando el nombre del producto asociado.

    Args:
        db: Objeto de conexión a la base de datos.

    Returns:
        list: Movimientos con el campo 'productoNombre' incluido.
    """
    pipeline = [
        {
            "$lookup": {
                "from": "productos",
                "localField": "productoId",
                "foreignField": "_id",
                "as": "producto"
            }
        },
        {
            "$unwind": {
                "path": "$producto",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$addFields": {
                "nombreProducto": "$producto.nombre"
            }
        },
        {
            "$project": {
                "producto": 0
            }
        }
    ]

    return list(db.movimientos.aggregate(pipeline))


def movimientos_por_fecha(db, fecha_inicio, fecha_fin):
    """
    Filtra los movimientos dentro de un intervalo de fechas, incluyendo el nombre del producto.

    Args:
        db: Conexión con la base de datos MongoDB.
        fecha_inicio: Fecha inicial (datetime).
        fecha_fin: Fecha final (datetime).

    Returns:
        list: Movimientos filtrados con nombre del producto incluido.
    """
    pipeline = [
        {
            "$match": {
                "fecha": {
                    "$gte": fecha_inicio,
                    "$lte": fecha_fin
                }
            }
        },
        {
            "$lookup": {
                "from": "productos",
                "localField": "productoId",
                "foreignField": "_id",
                "as": "producto"
            }
        },
        {
            "$unwind": {
                "path": "$producto",
                "preserveNullAndEmptyArrays": True
            }
        },
        {
            "$addFields": {
                "nombreProducto": "$producto.nombre"
            }
        },
        {
            "$project": {
                "producto": 0
            }
        }
    ]

    return list(db.movimientos.aggregate(pipeline))


def registrar_movimiento(db, datos_movimiento):
    """
    Agrega un nuevo movimiento en la colección correspondiente y ajusta el stock del producto.

    Args:
        db: Conexión a la base de datos.
        datos_movimiento (dict): Información del movimiento a registrar.

    Raises:
        ValueError: Si falta el identificador del producto.

    Returns:
        str: ID del documento insertado.
    """
    if "productoId" not in datos_movimiento:
        raise ValueError("Falta el campo obligatorio 'productoId'")

    datos_movimiento["productoId"] = ObjectId(datos_movimiento["productoId"])
    datos_movimiento["fecha"] = datetime.now()

    if datos_movimiento["tipo"] == "entrada":
        actualizado = model_producto.modificar_stock(db, datos_movimiento["productoId"], datos_movimiento["cantidad"])
    elif datos_movimiento["tipo"] == "salida":
        actualizado = model_producto.modificar_stock(db, datos_movimiento["productoId"], -int(datos_movimiento["cantidad"]))
    else:
        raise ValueError("El tipo de movimiento debe ser 'entrada' o 'salida'")

    if actualizado:
        resultado = db.movimientos.insert_one(datos_movimiento)
        return str(resultado.inserted_id)
