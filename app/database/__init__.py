from flask import g
import sqlite3

DATABASE_URI = "main.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URI)
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE_URI)
    return db
