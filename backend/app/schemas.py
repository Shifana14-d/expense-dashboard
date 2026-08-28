from pydantic import BaseModel


class ExpensesCreate(Basemodel):
    title: str
    amount: float
    category: str