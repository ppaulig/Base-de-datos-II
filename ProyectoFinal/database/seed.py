from bson import ObjectId
from datetime import datetime

def seed_data(db):

    if db.products.count_documents({}) == 0 and db.suppliers.count_documents({}) == 0 and db.movements.count_documents({}) == 0:
        id_producto = ObjectId()
        id_proveedor = ObjectId()

        db.products.insert_one({
            "_id": id_producto,
            "codigo": "PROD1001",
            "nombre": "Mouse Logitech M170",
            "categoria": "Periféricos",
            "precio": 19.99,
            "stockActual": 40,
            "stockMinimo": 10,
            "proveedorId": id_proveedor,
            "fechaUltimaActualizacion": datetime.utcnow()
        })

        db.movements.insert_one({
            "_id": ObjectId(),
            "productoId": id_producto,
            "tipo": "entrada",
            "cantidad": 25,
            "motivo": "Reabastecimiento mensual",
            "fecha": datetime.utcnow(),
            "usuario": "soporte_tienda"
        })

        db.suppliers.insert_one({
            "_id": id_proveedor,
            "nombre": "Mayorista GlobalTech",
            "contacto": "Mariana Silva",
            "telefono": "+54 11 5234-9876",
            "email": "contacto@globaltech.com",
            "productosOfrecidos": ["PROD1001", "PROD1002", "PROD1003"]
        })
        print("Datos seed insertados")
