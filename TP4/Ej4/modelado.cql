// Estudiantes
CREATE 
    (:Estudiante {nombre: 'Juan'}),
    (:Estudiante {nombre: 'María'}),
    (:Estudiante {nombre: 'Carlos'});

// Materias
CREATE 
    (:Materia {nombre: 'Literatura'}),
    (:Materia {nombre: 'Historia'}),
    (:Materia {nombre: 'Ingles'});

// Cursos 
CREATE 
    (:Curso {nombre: 'Ingles-b1'}),
    (:Curso {nombre: 'Ingles-b2'}),
    (:Curso {nombre: 'La Revolucion de Mayo'}),
    (:Curso {nombre: 'Mitologia Griega'});



// Inscripciones de alumnos en Cursos
MATCH (j:Estudiante {nombre: 'Juan'}) 
MATCH (b1:Curso {nombre: 'Ingles-b1'}) 
MATCH(r:Curso {nombre: 'La Revolucion de Mayo'}) 
MATCH (l:Curso {nombre: 'Mitologia Griega'})
CREATE 
    (j)-[:INSCRIPCION]->(b1), 
    (j)-[:INSCRIPCION]->(r), 
    (j)-[:INSCRIPCION]->(l);

MATCH (m:Estudiante {nombre: 'María'}) 
MATCH (b2:Curso {nombre: 'Ingles-b2'}) 
MATCH (r:Curso {nombre: 'La Revolucion de Mayo'}) 
MATCH (l:Curso {nombre: 'Mitologia Griega'})
CREATE 
    (m)-[:INSCRIPCION]->(b2), 
    (m)-[:INSCRIPCION]->(r), 
    (m)-[:INSCRIPCION]->(l);

MATCH (c:Estudiante {nombre: 'Carlos'}) 
MATCH (b2:Curso {nombre: 'Ingles-b2'})
CREATE 
    (c)-[:INSCRIPCION]->(b2);


// Cursos correspondientes a Materias
MATCH 
    (b1:Curso {nombre: 'Ingles-b1'}), 
    (i:Materia {nombre: 'Ingles'})
CREATE 
    (b1)-[:CORRESPONDE]->(i);

MATCH 
    (b2:Curso {nombre: 'Ingles-b2'}), 
    (i:Materia {nombre: 'Ingles'})
CREATE 
    (b2)-[:CORRESPONDE]->(i);

MATCH 
    (r:Curso {nombre: 'La Revolucion de Mayo'}), 
    (h:Materia {nombre: 'Historia'})
CREATE 
    (r)-[:CORRESPONDE]->(h);

MATCH 
    (m:Curso {nombre: 'Mitologia Griega'}), 
    (l:Materia {nombre: 'Literatura'})
CREATE 
    (m)-[:CORRESPONDE]->(l);


//Calificaciones de estudiantes en Materias
MATCH (j:Estudiante {nombre: 'Juan'}) 
MATCH (i:Materia {nombre: 'Ingles'}) 
MATCH (h:Materia {nombre: 'Historia'}) 
MATCH (l:Materia {nombre: 'Literatura'})
CREATE 
    (j)-[:CALIFICACION {nota: 10}]->(i), 
    (j)-[:CALIFICACION {nota: 8}]->(h), 
    (j)-[:CALIFICACION {nota: 7}]->(l);

MATCH (m:Estudiante {nombre: 'María'}) 
MATCH (i:Materia {nombre: 'Ingles'}) 
MATCH (h:Materia {nombre: 'Historia'}) 
MATCH (l:Materia {nombre: 'Literatura'})
CREATE 
    (m)-[:CALIFICACION {nota: 8}]->(i), 
    (m)-[:CALIFICACION {nota: 8}]->(h), 
    (m)-[:CALIFICACION {nota: 6}]->(l);

MATCH 
    (c:Estudiante {nombre: 'Carlos'}), 
    (i:Curso {nombre: 'Ingles'})
CREATE 
    (c)-[:CALIFICACION {nota: 7}]->(i);


// Prerrequisitos de Materias
MATCH
    (l:Materia {nombre: 'Literatura'}), (h:Materia {nombre: 'Historia'})
CREATE 
    (l)-[:PRERREQUISITO]->(h);