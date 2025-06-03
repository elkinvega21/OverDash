# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- ¡CAMBIOS REALIZADOS AQUÍ! ---
# Usuario: postgres
# Contraseña: vega123
# Host: host.docker.internal (para conexión desde Docker)
# Base de datos: fastapi_db
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:vega123@host.docker.internal:5432/fastapi_db"
# ---------------------------------

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Importa tus modelos para que Base los conozca.
# Asegúrate de que 'app.models.user' sea la ruta correcta a tu archivo de modelo de usuario.
from app.models import user