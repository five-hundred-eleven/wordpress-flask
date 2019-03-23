from pythonwp import app
from flask import abort, jsonify, request

tasks = [
        {
            'id': 1,
            'title': 'sleep',
            'description': 'zzzz',
            'done': False
        }, {
            'id': 2,
            'title': 'eat',
            'description': 'numnumnum',
            'done': True
        }, {
            'id': 3,
            'title': 'shower',
            'description': 'shhhhhhhhhhhhhhh',
            'done': False
        }
]

nextId = lambda: max([task['id'] for task in tasks])+1

@app.route('/')
@app.route('/index')
def index():
    return "hello world!";

@app.route('/tasks', methods=['GET'])
def getTasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def getTaskByTaskId(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)

    abort(404)

@app.route('/tasks', methods=['POST'])
def createTask():
    if not request.json or 'title' not in request.json:
        abort(400)
    task = {
            'id': nextId(),
            'title': request.json['title'],
            'description': request.json['description'],
            'done': False
    }
    tasks.append(task)
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def updateTask(task_id):
    if not request.json:
        abort(400)
    task = [task for task in tasks if task['id'] == task_id]
    if not task:
        abort(400)
    task = task[0]

    if 'title' in request.json:
        task['title'] = request.json['title']
    if 'description' in request.json:
        task['description'] = request.json['description']
    if 'done' in request.json and type(request.json['done']) is bool:
        task['done'] = request.json['done']

    return jsonify(task)

