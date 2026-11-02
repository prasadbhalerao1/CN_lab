# Experiment 6, Task 3: TCP Calculator Client

import socket
import sys

# Usage: python calc_client.py [server_ip]   (no IP = same computer)
HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 5002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

num1 = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /): ")
num2 = input("Enter second number: ")

message = num1 + " " + operator + " " + num2
client.sendall(message.encode())

result = client.recv(1024).decode()
print("Result:", result)

client.close()
