// Estudiantes
CREATE (:Estudiante { nombre: "Ana", carrera: "Ingeniería" });

CREATE (:Estudiante { nombre: "Luis", carrera: "Arquitectura" });

CREATE (:Estudiante { nombre: "Marta", carrera: "Derecho" });

// Libros
CREATE (:Libro { titulo: "Bases de Datos", categoria: "Tecnología" });

CREATE (:Libro { titulo: "Historia Argentina", categoria: "Historia" });

CREATE (:Libro { titulo: "Derecho Penal", categoria: "Derecho" });

CREATE (:Libro { titulo: "Diseño Moderno", categoria: "Diseño" });

// Préstamos
MATCH (e:Estudiante { nombre: "Ana" }), (l:Libro {titulo: "Bases de Datos"})
CREATE (e)-[:PRESTO { fecha: date("2025-06-15"), estado: "Activo" }]->(l);

MATCH (e:Estudiante { nombre: "Luis" }), (l:Libro {titulo: "Historia Argentina"})
CREATE (e)-[:PRESTO { fecha: date("2025-06-01"), estado: "Devuelto" }]->(l);

MATCH (e:Estudiante { nombre: "Marta" }), (l:Libro {titulo: "Derecho Penal"})
CREATE (e)-[:PRESTO { fecha: date("2025-06-20"), estado: "Activo" }]->(l);

MATCH (e:Estudiante { nombre: "Luis" }), (l:Libro {titulo: "Diseño Moderno"})
CREATE (e)-[:PRESTO { fecha: date("2025-06-22"), estado: "Activo" }]->(l);

MATCH (e:Estudiante { nombre: "Ana" }), (l:Libro {titulo: "Historia Argentina"})
CREATE (e)-[:PRESTO { fecha: date("2025-06-25"), estado: "Devuelto" }]->(l);

