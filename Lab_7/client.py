# Experiment 7: SSL/TLS Secure Client

import socket
import ssl
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder

# Usage: python client.py [server_ip]   (no IP = same computer)
HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 8443

context = ssl.create_default_context(cafile="server.crt")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

secure_client = context.wrap_socket(
    client, server_hostname="localhost"
)

print("Connected securely!")
print("TLS Version:", secure_client.version())

secure_client.sendall("Hello Server!".encode())

response = secure_client.recv(1024).decode()
print("Server:", response)

secure_client.close()
