from sqlalchemy import Boolean, Column, Integer, String
from ..database import Base # Asumiendo que database.py está en app/ y define Base

class User(Base): # <--- ASEGÚRATE DE QUE ESTA CLASE SE LLAME 'User'
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True) # Asegúrate de tener este campo si lo usas
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    full_name = Column(String, nullable=True) # Si tienes este campo

    # Aquí podrías tener relaciones, ej:
    # items = relationship("Item", back_populates="owner")