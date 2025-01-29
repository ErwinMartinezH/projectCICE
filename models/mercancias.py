from pydantic import BaseModel
from datetime import datetime

class Mercancia(BaseModel):
    descripcion: str
    tipo: str
    peso: float
    volumen: float
    fecha_ingreso: datetime
    fecha_salida: datetime = None
    deposito_id: int