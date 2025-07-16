from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
client_db = client["Inventario"]

if __name__ == "__main__":
    # test
    productos = client_db["productos"]
    print(list(productos.find({})))
