from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
tasks = []
class Task(Resource):
    def get(self, task_id):
        return tasks[task_id]
    def post(self, task_id):
        tasks[task_id] = request.form['data']
        return {'task_id': task_id, 'data': tasks[task_id]}
    def put(self, task_id):
        tasks[task_id] = request.form['data']
        return {'task_id': task_id, 'data': tasks[task_id]}
    api.add_resource(Task, '/tasks/<int:task_id>')
if __name__ == '__main__':
    app.run(debug=True)