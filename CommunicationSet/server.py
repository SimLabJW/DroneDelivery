from flask import Flask, request, jsonify

app = Flask(__name__)

# 전송된 데이터를 저장할 변수
unity_received_data = []
client_processed_data = []

@app.route('/sim/state/', methods=['POST'])
def send():
    global unity_received_data, client_processed_data
    if request.is_json:
        data = request.get_json()
        unity_received_data = data
        print(f"Received Data from Unity: \n{unity_received_data}")

        # 클라이언트가 보낸 데이터를 유니티로 전달하기 위해 response_data를 사용
        response_data = client_processed_data if client_processed_data else unity_received_data
        return jsonify(response_data)
    else:
        return jsonify({"message": "Invalid data format"}), 400

@app.route('/client/send', methods=['POST'])
def client_send():
    global client_processed_data
    if request.is_json:
        data = request.get_json()
        print(f"Received Data from Client: \n{data}")

        # 기존 데이터를 업데이트
        for new_item in data:
            for old_item in client_processed_data:
                if old_item['id'] == new_item['id']:
                    old_item.update(new_item)
                    break
            else:
                client_processed_data.append(new_item)

        response_data = {
            "status": "success",
            "message": "Data received from client"
        }
        return jsonify(response_data)
    else:
        return jsonify({"message": "Invalid data format"}), 400

@app.route('/client/receive', methods=['GET'])
def client_receive():
    global unity_received_data
    if unity_received_data:
        return jsonify(unity_received_data)
    else:
        return jsonify([])  # 빈 리스트를 반환하여 데이터가 없음을 나타냄

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the home page!"

def start():
    app.run(host='0.0.0.0', port=17148)

if __name__ == '__main__':
    start()
