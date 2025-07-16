from flask import Flask, render_template

from database.connection import client_db
from database.seed import seed_data
from routes.movements_routes import movimientos_bp
from routes.suppliers_routes import proveedores_bp
from routes.product_routes import productos_bp

app = Flask(__name__)

seed_data(client_db)

@app.route('/')
def home():
    return "Hola desde Flask en Windows!"

app.register_blueprint(productos_bp, url_prefix='/productos')
app.register_blueprint(proveedores_bp, url_prefix='/proveedores')
app.register_blueprint(movimientos_bp, url_prefix='/movimientos')



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)
