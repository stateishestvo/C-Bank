from sqlalchemy.orm import Session
from . import models, schemas
from .logger import logger

def get_user(db: Session, user_id: int):
    logger.info(f"Fetching user with id {user_id}")
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    logger.info(f"Fetching user with email {email}")
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f"Created user with id {db_user.id}")
    return db_user

def get_accounts(db: Session, skip: int = 0, limit: int = 10):
    logger.info(f"Fetching accounts with skip {skip} and limit {limit}")
    return db.query(models.Account).offset(skip).limit(limit).all()

def create_account(db: Session, account: schemas.AccountCreate):
    db_account = models.Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    logger.info(f"Created account with id {db_account.id}")
    return db_account

def get_transactions(db: Session, skip: int = 0, limit: int = 10):
    logger.info(f"Fetching transactions with skip {skip} and limit {limit}")
    return db.query(models.Transaction).offset(skip).limit(limit).all()

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    logger.info(f"Created transaction with id {db_transaction.id}")
    return db_transaction