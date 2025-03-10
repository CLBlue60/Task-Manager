from flask import Flask, request, jsonify
from .database import get_db_connection
from app.database import task

app = Flask(__name__)

@app.get("/")
@app.get("/tasks")
def get_tasks():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify({"tasks": [dict(task) for task in tasks]})

@app.get("/tasks/<int:pk>")
def get_task(pk):
    out = {
        "task": task.select_by_id(pk),
        "ok": True
    }
    return out

app.post("/tasks")
def create_task():
    task.create.task(request.json)
    return "", 204

app.put("/tasks/<int:pk>")
def update_task(pk):
    task.update_task_by_id(pk, request.json)
    return "", 204

app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete_task_by_id(pk)
    return "", 204
