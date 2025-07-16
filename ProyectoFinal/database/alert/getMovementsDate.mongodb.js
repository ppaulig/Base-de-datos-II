use('Inventario');

db.movimientos.aggregate([
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
                "productoNombre": "$producto.nombre"
            }
        },
        {
            "$project": {
                "producto": 0
            }
        }
    ])
