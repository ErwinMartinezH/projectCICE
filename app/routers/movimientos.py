from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Movimiento

router = APIRouter(prefix="/movimientos", tags=["Movimientos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_movimientos(db: Session = Depends(get_db)):
    return db.query(Movimiento).all()

@router.post("/")
def create_movimiento(movimiento: Movimiento, db: Session = Depends(get_db)):
    db.add(movimiento)
    db.commit()
    db.refresh(movimiento)
    return movimiento
