# Experiment 6, Task 1: TCP Hello Server

import socket
import os

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if os.name != "nt":  # Lets the server restart straight away on Linux
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print("Server is waiting for connection...")

conn, addr = server.accept()
print("Connected by:", addr)

message = conn.recv(1024).decode()
print("Client:", message)

conn.sendall("Hello Client!".encode())

conn.close()
server.close()
