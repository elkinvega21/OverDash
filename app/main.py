# En C:\Users\USUARIO\Downloads\backend\app\main.py
from fastapi import FastAPI
from .routes.user import router as user_router # <--- ¡CAMBIO CLAVE AQUÍ! El punto (.) al inicio

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola desde FastAPI en app/main.py con router de usuario!"}

# Incluimos el router de usuario.
# Considera añadir un prefijo para organizar mejor tus rutas, por ejemplo:
# app.include_router(user_router, prefix="/users", tags=["users"])
# Si no pones prefijo, las rutas de user_router se añadirán desde la raíz.
app.include_router(user_router)

print("User router incluido. Rutas en user_router:")
for route in user_router.routes:
    print(f"  Path: {route.path}, Name: {route.name}")