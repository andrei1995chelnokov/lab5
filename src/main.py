python
# src/main.py
from fastapi import FastAPI
from src.routers import user_router  # ← импортируем как user_router

app = FastAPI(title="User API", version="1.0")

# Подключаем роутер (передаём сам роутер, а не user_router.router)
app.include_router(user_router)  # ← убираем .router

@app.get("/")
def root():
    return {"message": "API is working"}
