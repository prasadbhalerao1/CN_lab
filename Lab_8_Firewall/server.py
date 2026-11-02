# Experiment 8: Firewall Testing - TCP Server

import socket
import os

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if os.name != "nt":  # Lets the server restart straight away on Linux
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print("Server is waiting for connection...")

while True:
    conn, addr = server.accept()
    print("Connected by:", addr)

    message = conn.recv(1024).decode()
    print("Client:", message)

    conn.sendall("Message received successfully!".encode())
    conn.close()
