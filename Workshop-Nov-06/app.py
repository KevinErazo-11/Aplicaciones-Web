import os

import psycopg
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/health")
def health():
    try:
        with psycopg.connect(
            host=os.getenv("POSTGRES_HOST", "db"),
            dbname=os.getenv("POSTGRES_DB", "postgres"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.environ["POSTGRES_PASSWORD"],
            connect_timeout=3,
        ) as conn:
            conn.execute("SELECT 1").fetchone()

    except psycopg.Error as exc:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        ) from exc

    return {
        "status": "ok",
        "version": "v2",
        "database": "ok"
    }
