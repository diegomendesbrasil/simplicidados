from sqlalchemy import Column, Integer, String, Date, Numeric
from .database import Base

class Expense(Base):
    __tablename__ = "despesa"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)
    payment_date = Column(Date, nullable=True)
    amount = Column(Numeric(10, 2), nullable=False)

class Revenue(Base):
    __tablename__ = "receita"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)
    receipt_date = Column(Date, nullable=True)
    amount = Column(Numeric(10, 2), nullable=False)
