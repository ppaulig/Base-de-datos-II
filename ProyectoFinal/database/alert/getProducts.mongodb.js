use('Inventario');

db.productos.aggregate([

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
            "preserveNullAndEmptyArrays": true
        }
    },
    {
        "$addFields": {
            "proveedorNombre": "$proveedor.nombre"
        }
    },

    {        "$project": {
            "proveedor": 0
        }
    }

])