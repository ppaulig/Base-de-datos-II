use("Inventario")

db.movimientos.aggregate([
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
                "preserveNullAndEmptyArrays": true
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