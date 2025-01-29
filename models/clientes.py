from pydantic import BaseModel

class Cliente(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    email: str