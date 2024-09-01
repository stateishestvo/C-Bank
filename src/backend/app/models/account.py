from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    account_type = Column(String, index=True)
    balance = Column(Float, default=0.0)
    account_number = Column(String, unique=True, index=True)

    user = relationship("User", backref="accounts")

    def __repr__(self):
        return f"<Account(id={self.id}, user_id={self.user_id}, 
        account_number={self.account_number}, balance={self.balance})>"