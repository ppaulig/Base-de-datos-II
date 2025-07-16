#Imagen base
FROM python:3.13.5-slim

#Crear directorio de trabajo
WORKDIR /app

#Copiar los archivos del proyecto
COPY . .

#Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Exponer el puerto
EXPOSE 5000

#Comando para iniciar Flask
CMD ["python", "app.py"]
