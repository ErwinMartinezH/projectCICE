from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.post("/")
def create_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario
