from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AccountBase(BaseModel):
    user_id: int  # Идентификатор пользователя, которому принадлежит счёт
    account_type: str  # Тип счёта (например, "checking", "savings")
    balance: float  # Баланс счёта
    account_number: str = Field(..., min_length=10, max_length=10)  # Номер счёта (10 символов)

class AccountCreate(AccountBase):
    pass

class AccountUpdate(BaseModel):
    account_type: Optional[str] = None  # Тип счёта (необязательное)
    balance: Optional[float] = None  # Баланс счёта (необязательное)
    
class AccountResponse(AccountBase):
    id: int  # Уникальный идентификатор счёта
    created_at: datetime  # Дата и время создания счёта

    class Config:
        orm_mode = True