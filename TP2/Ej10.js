use("TP2")

// Creamos usuario con permisos de lectura y escritura
db.createUser({
    user: "usuario_rw",
    pwd: "contraseña_segura",
    roles: [{ role: "readWrite", db: "empresa" }]
})

// Hacemos un backup desde la consola:
    // mongodump --db=TP2 --out=./backup

// Restauramos desde la consola:
    // mongorestore --db=TP2 ./backup/TP2
