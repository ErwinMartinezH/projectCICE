from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Cliente

router = APIRouter(prefix="/clientes", tags=["Clientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()

@router.post("/")
def create_cliente(cliente: Cliente, db: Session = Depends(get_db)):
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente
