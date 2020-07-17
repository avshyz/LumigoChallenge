from flask import Flask, request, jsonify

from src.logger import Logger
from src.manager import Manager
from src.task import Task

app = Flask(__name__)
manager = None


@app.route('/statistics', methods=["GET"])
def get_statistics():
    return jsonify({
        'active_instances': len([c for c in manager.consumers if c.is_alive()]),
        'total_invocation': manager.invocation_count.value(),
    })


@app.route('/messages', methods=["POST"])
def enqueue_message():
    data = request.get_json()
    manager.enqueue_task(Task(data['message']))
    return 200


if __name__ == '__main__':
    manager = Manager(Logger())
    manager.start()
    app.run(port=5000, debug=True)
