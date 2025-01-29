from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/depositos/", response_model=schemas.Deposito)
def create_deposito(deposito: schemas.DepositoCreate, db: Session = Depends(get_db)):
    return crud.create_deposito(db=db, deposito=deposito)

@app.get("/depositos/{deposito_id}", response_model=schemas.Deposito)
def read_deposito(deposito_id: int, db: Session = Depends(get_db)):
    db_deposito = crud.get_deposito(db, deposito_id=deposito_id)
    if db_deposito is None:
        raise HTTPException(status_code=404, detail="Deposito not found")
    return db_deposito

# Define más endpoints para las otras tablas...