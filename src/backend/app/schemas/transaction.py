from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    sender_id: int  # Идентификатор отправителя
    receiver_id: int  # Идентификатор получателя
    amount: float  # Сумма транзакции
    transaction_type: str  # Тип транзакции (например, "transfer", "deposit", "withdrawal")

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(BaseModel):
    status: Optional[str] = None  # Статус транзакции (например, "pending", "completed", "failed")

class TransactionResponse(TransactionBase):
    id: int  # Уникальный идентификатор транзакции
    status: str  # Статус транзакции
    created_at: datetime  # Дата и время создания транзакции

    class Config:
        orm_mode = True