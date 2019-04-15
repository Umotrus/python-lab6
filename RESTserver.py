from flask import Flask, request, jsonify
import db_interaction


api_endpoint = "/tasksApi/v1"  # http://localhost:5000  ,
app = Flask(__name__)


@app.route(api_endpoint+"/tasks", methods=["GET", "POST"])
def get_task_list():
    if request.method == "GET":
        tasks = db_interaction.get_sorted_tasks_list()
        return jsonify(tasks)
    else:  # POST request: use header Content-Type: application/json
        new_task = request.json
        db_interaction.db_insert_task(new_task['description'], new_task['urgent'])
        return ""


@app.route(api_endpoint+"/tasks/<int:task_id>", methods=["GET", "PUT", "DELETE"])
def get_one_task(task_id):
    if request.method == "GET":
        return jsonify(db_interaction.get_task(task_id))
    elif request.method == "PUT":
        content = request.json
        db_interaction.update_task(task_id, content["description"], content["urgent"])
        return ""
    elif request.method == "DELETE":
        db_interaction.db_remove_task(task_id)
    return ""


if __name__ == '__main__':
    app.run()
