from bson import ObjectId
from datetime import datetime

from models import products

def listar_movimientos(db):

    pipeline = [
        {
            "$lookup": {
                "from": "products",
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

    return list(db.movements.aggregate(pipeline))


def movimientos_por_fecha(db, fecha_inicio, fecha_fin):

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
                "from": "products",
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

    return list(db.movements.aggregate(pipeline))


def registrar_movimiento(db, datos_movimiento):

    if "productoId" not in datos_movimiento:
        raise ValueError("Falta el campo obligatorio 'productoId'")

    datos_movimiento["productoId"] = ObjectId(datos_movimiento["productoId"])
    datos_movimiento["fecha"] = datetime.now()

    if datos_movimiento["tipo"] == "entrada":
        actualizado = products.actualizar_stock(db, datos_movimiento["productoId"], datos_movimiento["cantidad"])
    elif datos_movimiento["tipo"] == "salida":
        actualizado = products.actualizar_stock(db, datos_movimiento["productoId"], -int(datos_movimiento["cantidad"]))
    else:
        raise ValueError("El tipo de movimiento debe ser 'entrada' o 'salida'")

    if actualizado:
        resultado = db.movements.insert_one(datos_movimiento)
        return str(resultado.inserted_id)
