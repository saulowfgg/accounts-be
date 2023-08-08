import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB = os.getenv("MONGO_DB")
    MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")
    APP_VERSION = os.getenv("APP_VERSION")
    HOST: str = os.getenv("APP_HOST")
    PORT: int  = os.getenv("APP_PORT")