# Usa una imagen liviana de Python
FROM python:3.10-slim

# Directorio dentro del contenedor
WORKDIR /app

# Copia los archivos al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de Flask
EXPOSE 5000

# Comando que ejecuta la app
CMD ["python", "app.py"]
