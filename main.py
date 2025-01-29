from fastapi import FastAPI
from .routers import auth, depositos

app = FastAPI()

app.include_router(auth.router)
app.include_router(depositos.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la plataforma de depósitos masivos"}