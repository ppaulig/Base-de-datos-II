id_producto = ObjectId();
id_proovedor = ObjectId();
id_movimiento = ObjectId();

// Insertar producto
db.products.insertOne({
  _id: id_producto,
  codigo: "PROD2025",
  nombre: "Teclado Mecánico Redragon K552",
  categoria: "Periféricos",
  precio: 54.99,
  stockActual: 30,
  stockMinimo: 8,
  proveedorId: id_proovedor,
  fechaUltimaActualizacion: ISODate()
});

// Insertar movimiento
db.movements.insertOne({
  _id: id_movimiento,
  productoId: id_producto,
  tipo: "entrada", // "entrada" o "salida"
  cantidad: 20,
  motivo: "Nuevo ingreso de stock",
  fecha: ISODate(),
  usuario: "inventario_admin"
});

// Insertar proveedor
db.suppliers.insertOne({
  _id: id_proovedor,
  nombre: "Importadora TecnoPlus",
  contacto: "Carla Méndez",
  telefono: "+54 11 4567-8910",
  email: "carla@tecnoplus.com.ar",
  productosOfrecidos: ["PROD2025", "PROD2026"]
});