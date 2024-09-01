from pydantic import BaseModel
from datetime import datetime

class SavingsAccountBase(BaseModel):
    user_id: int
    initial_amount: float
    current_amount: float
    created_at: datetime

class SavingsAccountCreate(SavingsAccountBase):
    pass

class SavingsAccount(SavingsAccountBase):
    id: int

    class Config:
        orm_mode = True