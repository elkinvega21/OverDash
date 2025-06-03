from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    # Aquí podrías agregar lógica para hashear la contraseña si quieres
    db_user = models.User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        password=user.password  # ¡No es seguro guardar texto plano!
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
