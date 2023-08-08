from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.collection import Collection
from app.config import Config

app = FastAPI()

# Configurações do MongoDB
MONGO_URI = Config.MONGO_URI
MONGO_DB = Config.MONGO_DB
MONGO_COLLECTION = Config.MONGO_COLLECTION
MONGO_COUNTERS_COLLECTION = "counters"

# Conexão com o MongoDB
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection: Collection = db[MONGO_COLLECTION]
counters_collection: Collection = db[MONGO_COUNTERS_COLLECTION]

from app.database import counters_collection

# Criação de um documento inicial na coleção de contadores
if "account_id" not in counters_collection.distinct("_id"):
    counters_collection.insert_one({"_id": "account_id", "seq": 0})
