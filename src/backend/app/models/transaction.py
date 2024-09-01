from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), index=True)
    receiver_id = Column(Integer, ForeignKey("users.id"), index=True)
    amount = Column(Float, nullable=False)
    transaction_type = Column(String, index=True)
    status = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    sender = relationship("User", foreign_keys=[sender_id], backref="sent_transactions")
    receiver = relationship("User", foreign_keys=[receiver_id], backref="received_transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, sender_id={self.sender_id}, receiver_id={self.receiver_id}, amount={self.amount})>"
    