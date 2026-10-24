import os

from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv("DATABASE_URL")

engine = (
    create_engine(DATABASE_URL, pool_pre_ping=True)
    if DATABASE_URL
    else None
)


def test_database_connection() -> int:
    if engine is None:
        raise RuntimeError("DATABASE_URL is not configured.")

    with engine.connect() as connection:
        return connection.execute(text("SELECT 1")).scalar_one()
