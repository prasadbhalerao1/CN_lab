# Experiment 9: Web Client using TCP Socket

import socket
import sys

# Usage: python client.py [server_ip]   (no IP = same computer)
HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

request = (
    "GET /index.html HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "Connection: close\r\n\r\n"
)

client.sendall(request.encode())

response = b""
while True:
    data = client.recv(1024)
    if not data:
        break
    response += data

print(response.decode(errors="replace"))
client.close()
