from fastapi import FastAPI
from src.routers import user  # ← импортируем как user (или как назван объект в __init__.py)

app = FastAPI(title="User API", version="1.0")

app.include_router(user)  # ← используем user

@app.get("/")
def root():
    return {"message": "API is working"}
