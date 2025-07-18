use('InventarioTienda');

db.products.aggregate([

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