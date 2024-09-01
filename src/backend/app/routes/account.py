from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.account import Account
from app.schemas.account import AccountCreate, AccountUpdate, AccountResponse

router = APIRouter()

@router.post("/accounts", response_model=AccountResponse)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

@router.get("/accounts/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db)):
    db_account = db.query(Account).filter(Account.id == account_id).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.put("/accounts/{account_id}", response_model=AccountResponse)
def update_account(account_id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    db_account = db.query(Account).filter(Account.id == account_id).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    for key, value in account.dict().items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return db_account

@router.delete("/accounts/{account_id}")
def delete_account(account_id: int, db: Session = Depends(get_db)):
    db_account = db.query(Account).filter(Account.id == account_id).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    db.delete(db_account)
    db.commit()
    return {"detail": "Account deleted"}