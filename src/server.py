
from flask import Flask, request, jsonify

from logger import Logger
from manager import Manager
from task import Task

app = Flask(__name__)
manager = None


@app.route('/statistics', methods=["GET"])
def get_statistics():
    return jsonify({
        'active_instances': manager.get_running_tasks(),
        'total_invocation': manager.invocation_count.value(),
    })


@app.route('/messages', methods=["POST"])
def enqueue_message():
    data = request.get_json()
    manager.enqueue_task(Task(data['message']))
    return 'OK', 200

if __name__ == '__main__':
    manager = Manager(logger=Logger('./log.txt'))
    manager.start()
    app.run(port=5000, debug=True)
