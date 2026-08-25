from fastapi import FastAPI

app= FastAPI(title="Expense Dashboard API")

@app.get("/")
def home():
    return {
        "message": "Expense Dashboard API is running!"    
    }


@app.get("/health")
def health_check():
    return{
        "status": "Healthy"
    }
    
