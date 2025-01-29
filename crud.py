from sqlalchemy.orm import Session
from . import models, schemas

def get_deposito(db: Session, deposito_id: int):
    return db.query(models.Deposito).filter(models.Deposito.id == deposito_id).first()

def create_deposito(db: Session, deposito: schemas.DepositoCreate):
    db_deposito = models.Deposito(**deposito.dict())
    db.add(db_deposito)
    db.commit()
    db.refresh(db_deposito)
    return db_deposito

# Define más funciones CRUD para las otras tablas...