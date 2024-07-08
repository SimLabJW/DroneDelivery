import requests
import time

# 연결 기능
def http_connect():
    session = requests.Session()
    return session

# 주는 기능
def http_send(session, url, data):
    response = session.post(url, json=data)
    return response

# 받는 기능
def http_receive(session, url):
    response = session.get(url)
    return response.json()

# 해제 기능
def http_close(session):
    session.close()

# Example usage
http_session = http_connect()

try:
    while True:
        # 클라이언트에서 서버로 데이터 전송
        send_data = {
            "drone_id": "CL12345",
            "home": 1,
            "store": 2,
            "state": "active"
        }
        send_response = http_send(http_session, 'http://192.168.50.75:13158/client/send', send_data)
        print(f"Send response: {send_response.status_code}")

        # 서버로부터 응답 받기 (유니티가 요청하는 엔드포인트)
        receive_response = http_receive(http_session, 'http://192.168.50.75:13158/unity/receive')
        print(f"Receive response: {receive_response}")

        # 주기적으로 10초 대기 후 반복
        time.sleep(10)

except KeyboardInterrupt:
    # 프로그램 종료 시 세션 닫기
    http_close(http_session)
    print("Session closed.")
