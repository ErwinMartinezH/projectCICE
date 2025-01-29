from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base

class Deposito(Base):
    __tablename__ = "depositos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(200), nullable=False)
    capacidad_maxima = Column(Integer, nullable=False)
    estado = Column(Enum('activo', 'inactivo'), default='activo')

class Mercancia(Base):
    __tablename__ = "mercancias"
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(200), nullable=False)
    tipo = Column(Enum('importacion', 'exportacion'), nullable=False)
    peso = Column(Float, nullable=False)
    volumen = Column(Float, nullable=False)
    fecha_ingreso = Column(DateTime, nullable=False)
    fecha_salida = Column(DateTime, nullable=True)
    deposito_id = Column(Integer, ForeignKey('depositos.id'))
    deposito = relationship("Deposito")

class Movimiento(Base):
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True, index=True)
    mercancia_id = Column(Integer, ForeignKey('mercancias.id'))
    tipo_movimiento = Column(Enum('ingreso', 'salida'), nullable=False)
    fecha_movimiento = Column(DateTime, nullable=False)
    deposito_id = Column(Integer, ForeignKey('depositos.id'))
    cliente_id = Column(Integer, ForeignKey('clientes.id'))

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=True)
    telefono = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    rol = Column(Enum('admin', 'operador'), default='operador')