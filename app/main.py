from fastapi import FastAPI
from app.routes.user import router as user_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola desde FastAPI!"}

app.include_router(user_router)
