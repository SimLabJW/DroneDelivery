import zmq

# 연결 기능
def zmq_connect(host, port):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{host}:{port}")
    return socket

# 주는 기능
def zmq_send(socket, message):
    socket.send_string(message)

# 받는 기능
def zmq_receive(socket):
    message = socket.recv_string()
    return message

# 해제 기능
def zmq_close(socket):
    socket.close()

# Example usage
zmq_sock = zmq_connect('localhost', 12345)
zmq_send(zmq_sock, 'Hello, ZeroMQ')
print(zmq_receive(zmq_sock))
zmq_close(zmq_sock)
