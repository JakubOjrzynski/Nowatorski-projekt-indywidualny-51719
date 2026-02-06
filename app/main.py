from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/db")
def db_check():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )
    cur = conn.cursor()
    cur.execute("SELECT 1")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return {"db": result[0]}
