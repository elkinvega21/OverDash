# app/main.py

from fastapi import FastAPI
from app.routes.user import router as user_router
from app.database import Base, engine
from app.models import user # Asegúrate de que todos tus modelos estén importados aquí

# 1. ¡Define tu instancia de FastAPI primero!
app = FastAPI()

# 2. Incluye tus routers (esto puede ir antes o después del evento de startup,
# pero es buena práctica tenerlo cerca de la definición de 'app')
app.include_router(user_router, prefix="/users", tags=["users"])

# 3. Ahora puedes usar @app.on_event porque 'app' ya está definida
@app.on_event("startup")
def on_startup():
    print("Creando tablas de la base de datos si no existen...")
    # Asegúrate de que todos los modelos que quieres que se creen estén importados
    # en este archivo o en un archivo que este importe (como app.models.user)
    Base.metadata.create_all(bind=engine)
    print("Tablas de la base de datos verificadas/creadas.")

# Puedes añadir más rutas o lógica aquí si es necesario
@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a tu API de FastAPI!"}
