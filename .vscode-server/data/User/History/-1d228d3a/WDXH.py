import socket

# TCP 소켓 클라이언트 설정
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

# 서버에 데이터 전송 및 수신
client_socket.sendall(b'Hello, Server!')
data = client_socket.recv(1024)
print(f"받은 데이터: {data}")
client_socket.close()