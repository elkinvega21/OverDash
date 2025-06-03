from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# La importación 'from app import crud, schemas, database' es un poco inusual.
# Es más común hacer:
# from .. import crud, database # (si crud y database están en app/)
# from ..schemas import UserResponse, UserCreate # Importar específicamente lo que necesitas
# Pero si 'from app import ...' te funciona, está bien por ahora.
# Lo importante es que 'schemas' se resuelva a tu módulo app.schemas.
from app import crud, schemas, database


router = APIRouter(prefix="/users", tags=["users"])

# Dependencia para obtener sesión de BD
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UserResponse) # <--- CAMBIO AQUÍ
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    # Asegúrate que crud.create_user devuelve un objeto compatible con UserResponse
    return crud.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=schemas.UserResponse) # <--- CAMBIO AQUÍ
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user