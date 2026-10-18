
import os
import time

import mysql.connector
from fastapi import FastAPI, HTTPException
from mysql.connector import Error

app = FastAPI(title="SkillPilot Multi-Container API")

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
        database=os.getenv("DB_NAME", "skillpilot_db"),
    )

@app.get("/")
def home():
    return {
        "message": "SkillPilot FastAPI application is running!",
        "services": ["FastAPI", "MySQL", "Adminer"]
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/db-test")
def db_test():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return {"database": "connected", "mysql_version": version}
    except Error as exc:
        raise HTTPException(status_code=503, detail="Database connection failed") from exc
