from fastapi import FastAPI
from app.routers import depositos, clientes, mercancias, movimientos, usuarios
from app.database import engine, Base

app = FastAPI()

# Importar modelos y crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Incluir los routers
app.include_router(depositos.router)
app.include_router(clientes.router)
app.include_router(mercancias.router)
app.include_router(movimientos.router)
app.include_router(usuarios.router)

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}
