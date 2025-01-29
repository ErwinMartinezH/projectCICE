from pydantic import BaseModel

class Deposito(BaseModel):
    nombre: str
    ubicacion: str
    capacidad_maxima: int
    estado: str = "activo"