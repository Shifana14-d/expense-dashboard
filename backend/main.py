from fastapi import FastAPI
from routes.expenses import router as expenses_router
from backend.app.database import engine, Base
from backend.app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Dashboard API")

app.include_router(expenses_router)


@app.get("/")
def home():
    return {"message": "Expense Dashboard API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
