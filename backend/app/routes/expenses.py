from fastapi import APIRouter

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.get("/")
def get_expenses():
    return {
        "message": "Expenses route working"
    }