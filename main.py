from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os
from dotenv import load_dotenv
from models.depositos import Deposito
from models.clientes import Cliente
from models.mercancias import Mercancia
from models.movimientos import Movimiento
from models.usuarios import Usuario

load_dotenv()

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_ADDON_HOST"),
        user=os.getenv("MYSQL_ADDON_USER"),
        password=os.getenv("MYSQL_ADDON_PASSWORD"),
        database=os.getenv("MYSQL_ADDON_DB"),
        port=os.getenv("MYSQL_ADDON_PORT")
    )

@app.get("/check_db")
def check_database_connection():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        
        # Verificamos la conexión
        cursor.execute("SELECT 1")  
        
        # Obtener las tablas de la base de datos
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        db.close()
        
        # Devolver la información de la conexión y las tablas
        return {
            "status": "success",
            "message": "Conexión a la base de datos exitosa",
            "tables": [table[1] for table in tables]  # Solo el nombre de las tablas
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}



# Rutas para Depositos
@app.get("/depositos")
def get_depositos():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM depositos")
    depositos = cursor.fetchall()
    db.close()
    return depositos

@app.post("/depositos")
def create_deposito(deposito: Deposito):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO depositos (nombre, ubicacion, capacidad_maxima, estado) VALUES (%s, %s, %s, %s)",
        (deposito.nombre, deposito.ubicacion, deposito.capacidad_maxima, deposito.estado)
    )
    db.commit()
    db.close()
    return {"message": "Deposito creado exitosamente"}

# Rutas para Clientes
@app.get("/clientes")
def get_clientes():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    db.close()
    return clientes

@app.post("/clientes")
def create_cliente(cliente: Cliente):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO clientes (nombre, direccion, telefono, email) VALUES (%s, %s, %s, %s)",
        (cliente.nombre, cliente.direccion, cliente.telefono, cliente.email)
    )
    db.commit()
    db.close()
    return {"message": "Cliente creado exitosamente"}

# Rutas para Mercancias
@app.get("/mercancias")
def get_mercancias():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM mercancias")
    mercancias = cursor.fetchall()
    db.close()
    return mercancias

@app.post("/mercancias")
def create_mercancia(mercancia: Mercancia):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO mercancias (descripcion, tipo, peso, volumen, fecha_ingreso, fecha_salida, deposito_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (mercancia.descripcion, mercancia.tipo, mercancia.peso, mercancia.volumen, mercancia.fecha_ingreso, mercancia.fecha_salida, mercancia.deposito_id)
    )
    db.commit()
    db.close()
    return {"message": "Mercancia creada exitosamente"}

# Rutas para Movimientos
@app.get("/movimientos")
def get_movimientos():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM movimientos")
    movimientos = cursor.fetchall()
    db.close()
    return movimientos

@app.post("/movimientos")
def create_movimiento(movimiento: Movimiento):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO movimientos (mercancia_id, tipo_movimiento, fecha_movimiento, deposito_id, cliente_id) VALUES (%s, %s, %s, %s, %s)",
        (movimiento.mercancia_id, movimiento.tipo_movimiento, movimiento.fecha_movimiento, movimiento.deposito_id, movimiento.cliente_id)
    )
    db.commit()
    db.close()
    return {"message": "Movimiento creado exitosamente"}

# Rutas para Usuarios
@app.get("/usuarios")
def get_usuarios():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    db.close()
    return usuarios

@app.post("/usuarios")
def create_usuario(usuario: Usuario):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO usuarios (nombre, email, password, rol) VALUES (%s, %s, %s, %s)",
        (usuario.nombre, usuario.email, usuario.password, usuario.rol)
    )
    db.commit()
    db.close()
    return {"message": "Usuario creado exitosamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
