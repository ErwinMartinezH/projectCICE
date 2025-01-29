from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/depositos/", response_model=schemas.Deposito)
def create_deposito(deposito: schemas.DepositoBase, db: Session = Depends(get_db)):
    db_deposito = models.Deposito(**deposito.dict())
    db.add(db_deposito)
    db.commit()
    db.refresh(db_deposito)
    return db_deposito

@router.get("/depositos/", response_model=list[schemas.Deposito])
def read_depositos(db: Session = Depends(get_db)):
    return db.query(models.Deposito).all()