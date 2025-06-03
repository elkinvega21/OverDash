from sqlalchemy.orm import Session
from .. import models # Asumiendo que models.User está bien ahora
from ..schemas.user import UserCreate # O como importes tus esquemas

def get_user_by_email(db: Session, email: str): # <--- ¡ASEGÚRATE QUE ESTA FUNCIÓN EXISTA CON ESTE NOMBRE!
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = user.password + "_hashed" # ¡Recuerda hashear las contraseñas de verdad!
    db_user = models.User(
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ... otras funciones CRUD ...