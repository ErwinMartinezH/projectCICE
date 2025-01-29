from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, Enum, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import datetime
import enum

DATABASE_URL = "mysql+pymysql://uw6nj48z5vmcuehr:zJ83lyXVUS0VuNYUtWdo@bcgqrvgitynk8bd0hlfr-mysql.services.clever-cloud.com:3306/bcgqrvgitynk8bd0hlfr"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class EstadoDeposito(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"

class TipoMercancia(str, enum.Enum):
    importacion = "importacion"
    exportacion = "exportacion"

class TipoMovimiento(str, enum.Enum):
    ingreso = "ingreso"
    salida = "salida"

class RolUsuario(str, enum.Enum):
    admin = "admin"
    operador = "operador"

class Deposito(Base):
    __tablename__ = "depositos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(200), nullable=False)
    capacidad_maxima = Column(Integer, nullable=False)
    estado = Column(Enum(EstadoDeposito), default=EstadoDeposito.activo)

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200))
    telefono = Column(String(20))
    email = Column(String(100))

class Mercancia(Base):
    __tablename__ = "mercancias"
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(200), nullable=False)
    tipo = Column(Enum(TipoMercancia), nullable=False)
    peso = Column(DECIMAL(10, 2), nullable=False)
    volumen = Column(DECIMAL(10, 2), nullable=False)
    fecha_ingreso = Column(DateTime, default=datetime.datetime.utcnow)
    fecha_salida = Column(DateTime, nullable=True)
    deposito_id = Column(Integer, ForeignKey("depositos.id"))

class Movimiento(Base):
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True, index=True)
    mercancia_id = Column(Integer, ForeignKey("mercancias.id"), nullable=False)
    tipo_movimiento = Column(Enum(TipoMovimiento), nullable=False)
    fecha_movimiento = Column(DateTime, default=datetime.datetime.utcnow)
    deposito_id = Column(Integer, ForeignKey("depositos.id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    rol = Column(Enum(RolUsuario), default=RolUsuario.operador)

class DepositoSchema(BaseModel):
    nombre: str
    ubicacion: str
    capacidad_maxima: int
    estado: EstadoDeposito

class ClienteSchema(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    email: str

class MercanciaSchema(BaseModel):
    descripcion: str
    tipo: TipoMercancia
    peso: float
    volumen: float
    deposito_id: int

class MovimientoSchema(BaseModel):
    mercancia_id: int
    tipo_movimiento: TipoMovimiento
    deposito_id: int
    cliente_id: int

class UsuarioSchema(BaseModel):
    nombre: str
    email: str
    password: str
    rol: RolUsuario

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/depositos", response_model=List[DepositoSchema])
def get_depositos(db: Session = Depends(get_db)):
    return db.query(Deposito).all()

@app.post("/depositos")
def create_deposito(deposito: DepositoSchema, db: Session = Depends(get_db)):
    nuevo_deposito = Deposito(**deposito.dict())
    db.add(nuevo_deposito)
    db.commit()
    db.refresh(nuevo_deposito)
    return nuevo_deposito

@app.get("/clientes", response_model=List[ClienteSchema])
def get_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()

@app.post("/clientes")
def create_cliente(cliente: ClienteSchema, db: Session = Depends(get_db)):
    nuevo_cliente = Cliente(**cliente.dict())
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente

@app.get("/mercancias", response_model=List[MercanciaSchema])
def get_mercancias(db: Session = Depends(get_db)):
    return db.query(Mercancia).all()

@app.post("/mercancias")
def create_mercancia(mercancia: MercanciaSchema, db: Session = Depends(get_db)):
    nueva_mercancia = Mercancia(**mercancia.dict())
    db.add(nueva_mercancia)
    db.commit()
    db.refresh(nueva_mercancia)
    return nueva_mercancia

@app.get("/movimientos", response_model=List[MovimientoSchema])
def get_movimientos(db: Session = Depends(get_db)):
    return db.query(Movimiento).all()

@app.post("/movimientos")
def create_movimiento(movimiento: MovimientoSchema, db: Session = Depends(get_db)):
    nuevo_movimiento = Movimiento(**movimiento.dict())
    db.add(nuevo_movimiento)
    db.commit()
    db.refresh(nuevo_movimiento)
    return nuevo_movimiento

@app.get("/usuarios", response_model=List[UsuarioSchema])
def get_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@app.post("/usuarios")
def create_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario
