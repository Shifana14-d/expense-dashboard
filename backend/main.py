from fastapi import FastAPI
from .database import engine, Base
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Dashboard API")


@app.get("/")
def home():
    return {"message": "Expense Dashboard API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
