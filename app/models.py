from typing import List
from pydantic import BaseModel



class Account(BaseModel):
    _id: int
    username: str
    password: str
    tagLine: str
    gameName: str
    accountId: int

class AccountListResponse(BaseModel):
    data: List[Account]
    total_documents: int
    total_filtered: int