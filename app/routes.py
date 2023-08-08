from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Account(BaseModel):
    id: int
    username: str
    password: str
    tagLine: str
    gameName: str

database = [
    Account(id=1, username="user1", password="pass1", tagLine="Tag 1", gameName="Game 1"),
    Account(id=2, username="user2", password="pass2", tagLine="Tag 2", gameName="Game 2"),
]

@router.get("/accounts/", response_model=List[Account])
def read_accounts(skip: int = 0, limit: int = 10):
    return database[skip : skip + limit]

@router.get("/accounts/{account_id}", response_model=Account)
def read_account(account_id: int):
    account = next((acc for acc in database if acc.id == account_id), None)
    if account is None:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return account

@router.post("/accounts/", response_model=Account)
def create_account(account: Account):
    account.id = len(database) + 1
    database.append(account)
    return account

@router.put("/accounts/{account_id}", response_model=Account)
def update_account(account_id: int, updated_account: Account):
    index = next((i for i, acc in enumerate(database) if acc.id == account_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    database[index] = updated_account
    return updated_account

@router.delete("/accounts/{account_id}", response_model=Account)
def delete_account(account_id: int):
    index = next((i for i, acc in enumerate(database) if acc.id == account_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    deleted_account = database.pop(index)
    return deleted_account
