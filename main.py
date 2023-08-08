from fastapi import FastAPI
from app.routes import router as app_router  # Importando as rotas do arquivo routes

app = FastAPI()

app.include_router(app_router, prefix="/app")  # Adicionando as rotas à instância FastAPI