from flask import Flask, request

app = Flask(__name__)


@app.route('/statisics', methods=["GET"])
def get_statistics():
    return 'here there be stats'


@app.route('/messages', methods=["POST"])
def enqueue_message():
    data = request.get_json()
    print(data['message'])
    return 'here there be message'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
