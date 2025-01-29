from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

@router.post("/depositos/", response_model=schemas.Deposito)
def create_deposito(deposito: schemas.DepositoCreate, db: Session = Depends(database.get_db)):
    db_deposito = models.Deposito(**deposito.dict())
    db.add(db_deposito)
    db.commit()
    db.refresh(db_deposito)
    return db_deposito

@router.get("/depositos/", response_model=list[schemas.Deposito])
def read_depositos(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    depositos = db.query(models.Deposito).offset(skip).limit(limit).all()
    return depositos