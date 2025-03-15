from flask import Flask, request, jsonify
import logging
from app.database.task import scan, select_by_id, create_task as db_create_task, update_task_by_id, delete_task_by_id

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = scan()
    return jsonify({"tasks": tasks, "ok": True})

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task_data = select_by_id(task_id)
    if task_data:
        return jsonify({"task": task_data, "ok": True})
    return jsonify({"error": "Task not found", "ok": False}), 404

@app.route("/tasks", methods=["POST"])
def create_task_route():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided", "ok": False}), 400

    try:
        db_create_task(data)
        return jsonify({"message": "Task created", "ok": True}), 201
    except Exception as e:
        logging.error(f"Error creating task: {e}")
        return jsonify({"error": str(e), "ok": False}), 500

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided", "ok": False}), 400

    try:
        update_task_by_id(task_id, data)
        return jsonify({"message": "Task updated", "ok": True}), 200
    except Exception as e:
        logging.error(f"Error updating task {task_id}: {e}")
        return jsonify({"error": str(e), "ok": False}), 500

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        delete_task_by_id(task_id)
        return jsonify({"message": "Task deleted", "ok": True}), 200
    except Exception as e:
        logging.error(f"Error deleting task {task_id}: {e}")
        return jsonify({"error": str(e), "ok": False}), 500
