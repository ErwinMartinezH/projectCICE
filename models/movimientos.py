from pydantic import BaseModel
from datetime import datetime

class Movimiento(BaseModel):
    mercancia_id: int
    tipo_movimiento: str
    fecha_movimiento: datetime
    deposito_id: int
    cliente_id: int