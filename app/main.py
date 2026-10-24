from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import test_database_connection

from app.routers import calculator, history

app = FastAPI(title="Mini Calculator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculator.router)
app.include_router(history.router)
@app.get("/test-db")
def test_db():
    return {"db_result": test_database_connection()}