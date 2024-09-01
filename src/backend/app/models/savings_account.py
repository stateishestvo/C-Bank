from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class SavingsAccount(Base):
    __tablename__ = "savings_accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    initial_amount = Column(Float, nullable=False)
    current_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="savings_accounts")

    def __init__(self, user_id, initial_amount):
        self.user_id = user_id
        self.initial_amount = initial_amount
        self.current_amount = initial_amount

    def update_interest(self):
        current_date = datetime.utcnow()
        years_passed = (current_date - self.created_at).days / 365
        if years_passed >= 1:
            self.current_amount *= (1 + 0.07) ** int(years_passed)
            self.created_at = current_date

    def __repr__(self):
        return f"<SavingsAccount(id={self.id}, user_id={self.user_id}, current_amount={self.current_amount})>"