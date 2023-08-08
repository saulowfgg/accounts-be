from fastapi import APIRouter, HTTPException
from fastapi import Query
from app.database import collection as account_collection
from app.models import Account, AccountListResponse
from app.utils import increment_counter
from typing import List

router = APIRouter()

@router.get("/accounts/", response_model=AccountListResponse, tags=["Account"])
def read_accounts(
    skip: int = 0,
    limit: int = 10,
    username: str = Query(None),
    tagLine: str = Query(None),
    gameName: str = Query(None),
    accountId: int = Query(None)
):
    filters = {}
    if username:
        filters["username"] = username
    if tagLine:
        filters["tagLine"] = tagLine
    if gameName:
        filters["gameName"] = gameName
    if accountId:
        filters["_id"] = accountId
    
    total_documents = account_collection.count_documents({})
    total_filtered = account_collection.count_documents(filters)  # Contagem com os filtros
    
    accounts = account_collection.find(filters).skip(skip).limit(limit)
    accounts_list = [
        Account(**{**acc, "accountId": acc.pop('_id')})
        for acc in accounts
    ]
    
    response_data = {
        "data": accounts_list,
        "total_documents": total_documents,
        "total_filtered": total_filtered,
    }
    return AccountListResponse(**response_data)


@router.get("/accounts/{account_id}", response_model=Account, tags=["Account"])
def read_account(account_id: str):
    account = account_collection.find_one({"_id": int(account_id)})
    if account is None:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return account

@router.post("/accounts/", response_model=Account, tags=["Account"])
def create_account(account: Account):
    new_id = increment_counter("account_id")  # Obtém um novo ID sequencial
    account_data = account.dict()
    account_data["_id"] = new_id  # Atribui o ID sequencial ao campo _id
    inserted_account = account_collection.insert_one(account_data)
    return account

@router.put("/accounts/{account_id}", response_model=Account, tags=["Account"])
def update_account(account_id: str, updated_account: Account):
    updated_account_data = updated_account.dict()
    result = account_collection.update_one({"_id": int(account_id)}, {"$set": updated_account_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return updated_account

@router.delete("/accounts/{account_id}", response_model=Account, tags=["Account"])
def delete_account(account_id: str):
    deleted_account = account_collection.find_one_and_delete({"_id": int(account_id)})
    if deleted_account is None:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return deleted_account
