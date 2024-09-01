from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String, index=True)
    balance = Column(Float, default=0.0)
    login = Column(String, unique=True, index=True)
    password = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, full_name='{self.full_name}', 
        phone_number='{self.phone_number}', email='{self.email}', 
        role='{self.role}', balance={self.balance}, login='{self.login}')>"