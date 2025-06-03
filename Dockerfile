# Usa una imagen oficial de Python como base
# Se recomienda una versión específica de Python para mayor estabilidad
FROM python:3.11-slim-buster

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias
# Esto se hace antes de copiar el resto del código para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de tu aplicación al directorio de trabajo
# La carpeta 'app' contiene main.py, por lo que esta línea es suficiente.
COPY ./app /app/app

# --- ¡IMPORTANTE! Asegúrate de que la línea 'COPY main.py /app/main.py' NO esté aquí ---
# Si la tenías, bórrala o coméntala.
# ---------------------------------------------------------------------------------------

# Expone el puerto en el que Uvicorn escuchará
EXPOSE 8000

# Define el comando para ejecutar tu aplicación con Uvicorn
# La aplicación principal ahora estará en /app/app/main.py
# Por lo tanto, el comando debe ser "app.main:app"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
