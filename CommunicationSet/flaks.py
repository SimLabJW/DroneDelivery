from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    print(f"Received data: {data}")
    return jsonify({"status": "success"})

@app.route('/receive', methods=['GET'])
def receive():
    return jsonify({"message": "Hello, HTTP"})

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(port=13158)
