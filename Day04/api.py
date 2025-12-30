from flask import Flask, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.task_db
tasks_collection = db.tasks

@app.route('/tasks', methods=['GET'])
def get_tasks():
        tasks = []
        for task in tasks_collection.find():
            task["_id"] = str(task["_id"])
            tasks.append(task)
        return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = {
        "title": data["title"],
        "completed": False
    }
    tasks_collection.insert_one(task)
    return jsonify({"message": "Task added"}), 201

if __name__ == '__main__':
    app.run(debug=True)