from pydantic import BaseModel
from datetime import datetime

class DepositoBase(BaseModel):
    nombre: str
    ubicacion: str
    capacidad_maxima: int
    estado: str = 'activo'

class DepositoCreate(DepositoBase):
    pass

class Deposito(DepositoBase):
    id: int

    class Config:
        orm_mode = True

# Define más esquemas para las otras tablas...