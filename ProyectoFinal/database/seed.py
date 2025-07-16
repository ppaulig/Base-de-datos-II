from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
client_db = client["Inventario"]

if __name__ == "__main__":
    # test
    productos = client_db["productos"]
    print(list(productos.find({})))
from bson import ObjectId
from datetime import datetime

def seed_data(db):
    """
    Inserta datos de ejemplo en la base de datos si todas las colecciones están vacías.

    Args:
        db: Conexión a la base de datos MongoDB.
    """
    if db.productos.count_documents({}) == 0 and db.proveedores.count_documents({}) == 0 and db.movimientos.count_documents({}) == 0:
        id_producto = ObjectId()
        id_proveedor = ObjectId()

        db.productos.insert_one({
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

        db.movimientos.insert_one({
            "_id": ObjectId(),
            "productoId": id_producto,
            "tipo": "entrada",
            "cantidad": 25,
            "motivo": "Reabastecimiento mensual",
            "fecha": datetime.utcnow(),
            "usuario": "soporte_tienda"
        })

        db.proveedores.insert_one({
            "_id": id_proveedor,
            "nombre": "Mayorista GlobalTech",
            "contacto": "Mariana Silva",
            "telefono": "+54 11 5234-9876",
            "email": "contacto@globaltech.com",
            "productosOfrecidos": ["PROD1001", "PROD1002", "PROD1003"]
        })
        print("Datos seed insertados")
