from app.database import counters_collection
from pymongo.collection import Collection
from pymongo.collection import ReturnDocument  # Importe o ReturnDocument

def increment_counter(counter_name: str) -> int:
    result = counters_collection.find_one_and_update(
        {"_id": counter_name},
        {"$inc": {"seq": 1}},
        upsert=True,
        projection={"seq": True},
        return_document=ReturnDocument.AFTER  # Use o ReturnDocument.AFTER
    )
    return result["seq"]
