from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Deposito

router = APIRouter(prefix="/depositos", tags=["Depositos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_depositos(db: Session = Depends(get_db)):
    return db.query(Deposito).all()

@router.post("/")
def create_deposito(deposito: Deposito, db: Session = Depends(get_db)):
    db.add(deposito)
    db.commit()
    db.refresh(deposito)
    return deposito
