# Experiment 8: Firewall Testing - TCP Client

import socket
import sys

# Usage: python client.py [server_ip]   (no IP = same computer)
HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)

try:
    client.connect((HOST, PORT))
    print("Connected to server!")

    message = "Hello Server!"
    client.sendall(message.encode())

    response = client.recv(1024).decode()
    print("Server:", response)

except socket.timeout:
    print("Connection timed out! Firewall may be blocking traffic.")
except OSError as error:
    print("Connection failed:", error)
finally:
    client.close()
