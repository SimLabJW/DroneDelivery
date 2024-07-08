import socket

# 연결 기능
def udp_connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return sock

# 주는 기능
def udp_send(sock, host, port, message):
    sock.sendto(message.encode(), (host, port))

# 받는 기능
def udp_receive(sock, buffer_size=1024):
    data, addr = sock.recvfrom(buffer_size)
    return data.decode()

# 해제 기능
def udp_close(sock):
    sock.close()

# Example usage
udp_sock = udp_connect('localhost', 12345)
udp_send(udp_sock, 'localhost', 12345, 'Hello, UDP')
print(udp_receive(udp_sock))
udp_close(udp_sock)
