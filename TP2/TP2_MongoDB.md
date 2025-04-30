# TP2: MongoDB

## 1. Crear base de datos y colección de empleados

1. Creamos la base de datos `Empresa`.

2. Agregamos la colección `empleados` con 3 documentos (`nombre`, `edad` y `puesto`):

    ```javascript
    db.empleados.insertMany([
      { nombre: "Ana", edad: 28, puesto: "desarrollador" },
      { nombre: "Luis", edad: 35, puesto: "diseñador" },
      { nombre: "Carla", edad: 30, puesto: "pasante" }
    ])
    ```

3. Actualizamos la edad de **Ana**:

    ```javascript
    db.empleados.updateOne(
      { nombre: "Ana" },
      { $set: { edad: 29 } }
    )
    ```

4. Eliminamos el empleado con el puesto `"pasante"`:

    ```javascript
    db.empleados.deleteOne({ puesto: "pasante" })
    ```

Captura: `Capturas/Punto1/`

---

## 2. Consultar empleados cuya edad está entre 25 y 40 años:

```javascript
db.empleados.find({
  edad: { $gte: 25, $lte: 40 }
})
```

Captura: `Capturas/Punto2.png`

---

## 3. Recuperar nombre y puesto sin mostrar el `_id`:

```javascript
db.empleados.find(
  {},
  { _id: 0, nombre: 1, puesto: 1 }
)
```

Captura: `Capturas/Punto3.png`

---

## 4. Agregar campo `direccion` a todos los empleados:

```javascript
db.empleados.updateMany({}, {
  $set: {
    direccion: {
      calle: "Falsa 123",
      ciudad: "Springfield",
      codigo_postal: "1234"
    }
  }
})
```

Captura: `Capturas/Punto4.png`

---

## 5. Crear colección `ventas` y calcular total vendido por producto

```javascript
db.ventas.insertMany([
  { producto: "Manzana", cantidad: 10, precio_unitario: 2 },
  { producto: "Banana", cantidad: 5, precio_unitario: 1.5 },
  { producto: "Manzana", cantidad: 7, precio_unitario: 2 },
  { producto: "Naranja", cantidad: 3, precio_unitario: 2.5 },
  { producto: "Banana", cantidad: 8, precio_unitario: 1.5 }
]);
```

Consulta:

```javascript
db.ventas.aggregate([
  {
    $group: {
      _id: "$producto",
      cantidad_total_vendida: { $sum: "$cantidad" }
    }
  }
])
```

Captura: `Capturas/Punto5.png`

---

## 6. Crear colección `clientes` e índice

```javascript
db.clientes.insertMany([
  { nombre: "Juan", apellido: "Pérez", edad: 30 },
  { nombre: "Ana", apellido: "Gómez", edad: 25 },
  { nombre: "Luis", apellido: "Martínez", edad: 40 },
  { nombre: "Carla", apellido: "Pérez", edad: 35 },
  { nombre: "Lucía", apellido: "Gómez", edad: 28 },
  { nombre: "Pedro", apellido: "Martínez", edad: 50 }
])
```

Crear índice:

```javascript
db.clientes.createIndex({ apellido: 1, nombre: 1 });
```

---

## 7. Crear colecciones `cursos` y `alumnos` con referencias

```javascript
db.cursos.insertMany([
  { _id: 1, nombre: "Matemáticas", descripcion: "Curso de álgebra y geometría" },
  { _id: 2, nombre: "Física", descripcion: "Curso de mecánica y termodinámica" },
  { _id: 3, nombre: "Química", descripcion: "Curso de química orgánica e inorgánica" }
])
```

Alumnos con id referenciado a cursos:
```javascript
db.alumnos.insertMany([
  { nombre: "Juan", apellido: "Pérez", edad: 20, id_cursos: [1, 2] },
  { nombre: "Ana", apellido: "Gómez", edad: 22, id_cursos: [2, 3] },
  { nombre: "Luis", apellido: "Martínez", edad: 24, id_cursos: [1, 3] },
  { nombre: "Carla", apellido: "Pérez", edad: 21, id_cursos: [1] },
  { nombre: "Lucía", apellido: "Gómez", edad: 23, id_cursos: [3] }
])
```

---

## 8. Combinamos datos de `alumnos` y `cursos`

```javascript
db.alumnos.aggregate([
  {
    $lookup: {
      from: "cursos",
      localField: "id_cursos",
      foreignField: "_id",
      as: "cursos_info"
    }
  }
])
```

Captura: `Capturas/Punto8.png`

---

## 9. Ventajas de Replica Set y Sharding

  Las ventajas de usar Replica set es que sirve para tener copias de seguridad en tiempo real. Si un servidor falla, otro toma su lugar automáticamente. Se puede usar uno para escribir y otros para leer, así no se sobrecarga.
  El Sharding sirve para dividir la base de datos en partes y repartirla en varios servidores. Esto ayuda a manejar grandes volúmenes de datos sin que se vuelva lenta, porque cada servidor trabaja con una parte distinta.

---

## 10. Seguridad y Backups

### Crear usuario con permisos de lectura y escritura:

```javascript
db.createUser({
  user: "usuario_rw",
  pwd: "contraseña_segura",
  roles: [{ role: "readWrite", db: "empresa" }]
})
```

### Backup de la base de datos desde terminal:

```bash
mongodump --db Empresa --out C:\FACULTAD
```

### Restauración de la base de datos:

```bash
mongorestore --db Empresa C:\FACULTAD
```
