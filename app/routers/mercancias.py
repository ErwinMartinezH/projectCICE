from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Mercancia

router = APIRouter(prefix="/mercancias", tags=["Mercancias"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_mercancias(db: Session = Depends(get_db)):
    return db.query(Mercancia).all()

@router.post("/")
def create_mercancia(mercancia: Mercancia, db: Session = Depends(get_db)):
    db.add(mercancia)
    db.commit()
    db.refresh(mercancia)
    return mercancia
