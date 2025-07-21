# Proyecto Final 

#### Participantes:
- [Rodrigo Arrue]
- [Hernan Folik]
- [Paula General]
- [Juan Meunier]


# Sistema de Gestion de Tienda

Tecnologias utilizadas:

- [Python]
- [Flask]
- [MongoDB]
- [Docker]
- [Pymongo]

### Deploy del proyecto con `docker-compose`:
El proyecto está containerizado y puede iniciarse fácilmente usando docker-compose. Al ejecutar el comando, se crean dos contenedores: uno correspondiente a MongoDB y otro para la aplicación web desarrollada en Flask (configurada mediante un Dockerfile). La aplicación se conecta a la base de datos a través de Pymongo en los modelos, y las rutas importan estos modelos para realizar las operaciones necesarias.

Al levantar los contenedores, se ejecuta automáticamente un script que crea la base de datos, las colecciones requeridas y carga los datos iniciales.
Para iniciar el proyecto, utiliza:

```bash
docker-compose up
```

La web estará disponible en [localhost:5000](http://localhost:5000) y la base de datos se puede conectar usando la siguiente connection string:

```
mongodb://localhost:27017
```
### Estructura del proyecto:
```bash
Proyecto Final/
│   app.py
│   docker-compose.yml
│   Dockerfile
│   README.md
│   requirements.txt
├───database/
│   │   connection.py
│   │   seed.py
│   └───alert/
│           lowStack.mongodb.js
│           delete_all.mongodb.js
│           getMovements.mongodb.js
│           getMovementsDate.js
│           getProducts.mongodb.js       
│           init.mongodb.js
├───models/
│       movements.py
│       products.py
│       suppliers.py
├───routes/
│       movements_routes.py
│       products_routes.py
│       suppliers_routes.py

```

