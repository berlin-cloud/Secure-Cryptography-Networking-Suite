import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 3000))

server.listen(1)

print("Waiting for connection...")

conn, addr = server.accept()

print(f"Connected by {addr}")

data = conn.recv(1024)

print(data.decode())