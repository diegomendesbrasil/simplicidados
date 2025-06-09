from datetime import date
from pydantic import BaseModel

class ExpenseBase(BaseModel):
    description: str
    due_date: date
    payment_date: date | None = None
    amount: float

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True

class RevenueBase(BaseModel):
    description: str
    due_date: date
    receipt_date: date | None = None
    amount: float

class RevenueCreate(RevenueBase):
    pass

class Revenue(RevenueBase):
    id: int

    class Config:
        orm_mode = True
