# Imagen base oficial de Python
FROM python:3.11

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto al contenedor
COPY . .

# Instalar dependencias necesarias
RUN pip install --no-cache-dir fastapi uvicorn scikit-learn joblib numpy pydantic

# Exponer el puerto en el que correrá la app
EXPOSE 8000

# Comando para ejecutar la API con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]