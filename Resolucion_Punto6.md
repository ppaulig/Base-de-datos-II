Ejercicio 6:

-Creamos las tablas necesarias
CREATE TABLE Productos (
  id_producto SERIAL PRIMARY KEY,
  nombre VARCHAR(100)
);
CREATE TABLE Ventas (
  id SERIAL PRIMARY KEY,
  id_producto INT REFERENCES Productos(id_producto),
  fecha DATE,
  cantidad INT
);

-Vista de las ventas mensuales

CREATE VIEW VentasMensuales AS
SELECT 
  id_producto,
  DATE_TRUNC('month', fecha) AS mes,
  SUM(cantidad) AS total_vendido
FROM Ventas
GROUP BY id_producto, mes;

    Esta vista agrupa las ventas por producto y mes, y resume la cantidad total vendida por mes.

-Consulta para saber los 5 productos mas vendidos

SELECT 
  p.nombre, 
  SUM(vm.total_vendido) AS total_vendido
FROM VentasMensuales vm
JOIN Productos p ON p.id_producto = vm.id_producto
GROUP BY p.nombre
ORDER BY total_vendido DESC
LIMIT 5;

    Esta consulta usa la vista VentasMensuales, junta los totales por producto, y muestra el top 5 de productos más vendidos.