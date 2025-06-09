from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="SimPliciDados API")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = models.Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


@app.get("/expenses/", response_model=list[schemas.Expense])
def list_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()


@app.post("/revenues/", response_model=schemas.Revenue)
def create_revenue(revenue: schemas.RevenueCreate, db: Session = Depends(get_db)):
    db_revenue = models.Revenue(**revenue.dict())
    db.add(db_revenue)
    db.commit()
    db.refresh(db_revenue)
    return db_revenue


@app.get("/revenues/", response_model=list[schemas.Revenue])
def list_revenues(db: Session = Depends(get_db)):
    return db.query(models.Revenue).all()
