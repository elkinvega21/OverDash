# En app/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    # Para Pydantic V2
    model_config = {
        "from_attributes": True  # Reemplaza a orm_mode = True
    }