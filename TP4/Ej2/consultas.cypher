//Libros con préstamo activo
MATCH (e:Estudiante)-[p:PRESTO { estado: "Activo" }]->(l:Libro)
RETURN l.titulo, e.nombre, p.fecha;

//Cantidad de libros prestados por estudiante
MATCH (e:Estudiante)-[p:PRESTO]->(l:Libro)
RETURN e.nombre, COUNT(p) AS total_prestamos;

//Categorías con más préstamos activos
MATCH (e:Estudiante)-[p:PRESTO { estado: "Activo" }]->(l:Libro)
RETURN l.categoria, COUNT(*) AS prestamos_activos
 ORDER BY prestamos_activos DESC;

//Estudiantes sin préstamos activos
MATCH (e:Estudiante)
WHERE NOT (e)-[:PRESTO { estado: "Activo" }]->()
RETURN e.nombre;
