from flask import Flask, request, jsonify

app = Flask(__name__)

# 전송된 데이터를 저장할 변수
client_received_data = None

class Http_Server():
    @app.route('/send', methods=['POST'])
    def send():
        global client_received_data
        client_received_data = request.json
        print(f"Received Data from Unity: \n{client_received_data}")

        response_data = []
        if isinstance(client_received_data, list):
            for item in client_received_data:
                processed_item = {
                    "id": item.get('id', 'N/A'),
                    "home": item.get('home', 0),
                    "store": item.get('store', 0),
                    "state": "processed"
                }
                response_data.append(processed_item)
        else:
            response_data = {
                "id": client_received_data.get('id', 'N/A'),
                "home": client_received_data.get('home', 0),
                "store": client_received_data.get('store', 0),
                "state": "processed"
            }

        return jsonify(response_data)

    @app.route('/unity/receive', methods=['GET'])
    def unity_receive():
        global client_received_data
        if client_received_data:
            return jsonify(client_received_data)
        else:
            return jsonify({
                "id": "no_data",
                "home": 0,
                "store": 0,
                "state": "no_data"
            })

    @app.route('/client/send', methods=['POST'])
    def client_send():
        global client_received_data
        client_received_data = request.json
        print(f"Received Data from Client: \n{client_received_data}")

        response_data = {
            "status": "success",
            "message": "Data received from client"
        }

        return jsonify(response_data)

    @app.route('/receive', methods=['GET'])
    def receive():
        global client_received_data
        if client_received_data:
            response_data = {
                "id": client_received_data.get('id', 'N/A'),
                "home": client_received_data.get('home', 0),
                "store": client_received_data.get('store', 0),
                "state": client_received_data.get('state', 'N/A')
            }
            return jsonify(response_data)
        else:
            return jsonify({"message": "No data received"}), 404

    @app.route('/', methods=['GET'])
    def home():
        return "Welcome to the home page!"

    def start():
        app.run(host='192.168.50.75', port=13158)

Http_Server.start()
