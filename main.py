from fastapi import FastAPI
from app.routes import router as app_router  # Importando as rotas do arquivo routes
from app.database import app as mongo_app # Importanto configurações do MongoDB
from app.config import Config

app = FastAPI(
    title="accounts-be",
    version=Config.APP_VERSION,
    host=Config.HOST,
    port=Config.PORT
)

app.include_router(app_router, prefix="/api")  # Adicionando as rotas à instância FastAPI
app.mount("/mongo", mongo_app) # Adicionando condigurações do Mongo à instância FastAPI