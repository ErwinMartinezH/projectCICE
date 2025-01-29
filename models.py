from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from .database import Base

class Deposito(Base):
    __tablename__ = "depositos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(200), nullable=False)
    capacidad_maxima = Column(Integer, nullable=False)
    estado = Column(Enum('activo', 'inactivo'), default='activo')

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
    tipo = Column(Enum('importacion', 'exportacion'), nullable=False)
    peso = Column(Float, nullable=False)
    volumen = Column(Float, nullable=False)
    fecha_ingreso = Column(DateTime, nullable=False)
    fecha_salida = Column(DateTime)
    deposito_id = Column(Integer, ForeignKey('depositos.id'))

class Movimiento(Base):
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True, index=True)
    mercancia_id = Column(Integer, ForeignKey('mercancias.id'), nullable=False)
    tipo_movimiento = Column(Enum('ingreso', 'salida'), nullable=False)
    fecha_movimiento = Column(DateTime, nullable=False)
    deposito_id = Column(Integer, ForeignKey('depositos.id'), nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    rol = Column(Enum('admin', 'operador'), default='operador')