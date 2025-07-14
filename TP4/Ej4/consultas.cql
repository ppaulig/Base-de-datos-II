// Transcripción académica de un estudiante
MATCH (e:Estudiante {nombre: 'María'})-[n:CALIFICACION]->(m:Materia)
WITH  e.nombre as estudiante, n.nota as nota, m.nombre as materia
RETURN estudiante, materia, nota


// Verificar si un estudiante puede inscribirse en una materia (si aprobó los prerrequisitos)
MATCH (e:Estudiante {nombre: 'Juan'}), (m:Materia {nombre: 'Literatura'})
MATCH (m)-[:PRERREQUISITO]->(prereq:Materia)
OPTIONAL MATCH (e)-[cal:CALIFICACION]->(prereq)
WITH e, m, 
     CASE 
       WHEN cal IS NOT NULL AND cal.nota >= 6 THEN true
       ELSE false
     END AS puede_inscribirse
RETURN e.nombre AS estudiante,
       m.nombre AS materia,
       puede_inscribirse;

// Promedio de calificaciones por estudiante.
MATCH (e:Estudiante)-[c:CALIFICACION]->(m:Materia)
WITH AVG(c.nota) AS promedio, e.nombre as estudiante
RETURN estudiante, promedio

// Materias con promedio inferior a 7.
MATCH (e:Estudiante)-[c:CALIFICACION]->(m:Materia)
WITH AVG(c.nota) AS promedio, m.nombre as materia
WHERE promedio < 7
RETURN materia, promedio
