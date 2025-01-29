from pydantic import BaseModel
from datetime import datetime

class UsuarioBase(BaseModel):
    email: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    nombre: str
    rol: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

class DepositoBase(BaseModel):
    nombre: str
    ubicacion: str
    capacidad_maxima: int

class Deposito(DepositoBase):
    id: int
    estado: str

    class Config:
        orm_mode = True