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
        # 서버로 메시지 전송
        send_response = http_send(http_session, 'http://localhost:13158/send', {'message': 'Hello, HTTP'})
        print(f"Send response: {send_response.status_code}")

        # 서버로부터 응답 받기
        receive_response = http_receive(http_session, 'http://localhost:13158/receive')
        print(f"Receive response: {receive_response}")

        # 주기적으로 10초 대기 후 반복
        time.sleep(1)

except KeyboardInterrupt:
    # 프로그램 종료 시 세션 닫기
    http_close(http_session)
    print("Session closed.")
