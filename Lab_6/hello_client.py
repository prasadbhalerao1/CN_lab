# Experiment 6, Task 1: TCP Hello Client

import socket
import sys

# Usage: python hello_client.py [server_ip]   (no IP = same computer)
HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = "Hello Server!"
client.sendall(message.encode())

response = client.recv(1024).decode()
print("Server:", response)

client.close()
