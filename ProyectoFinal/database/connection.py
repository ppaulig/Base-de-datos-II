from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
client_db = client["InventarioTienda"]

if __name__ == "__main__":
    # test
    productos = client_db["products"]
    print(list(productos.find({})))
