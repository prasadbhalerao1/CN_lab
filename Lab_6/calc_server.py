# Experiment 6, Task 3: TCP Calculator Server

import socket
import os

HOST = "0.0.0.0"
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if os.name != "nt":  # Lets the server restart straight away on Linux
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print("Calculator Server is waiting...")
conn, addr = server.accept()
print("Connected by:", addr)

data = conn.recv(1024).decode()

try:
    num1, operator, num2 = data.split()
    num1 = float(num1)
    num2 = float(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Division by zero!"
    else:
        result = "Invalid operator!"
except ValueError:
    result = "Invalid input!"

conn.sendall(str(result).encode())
print("Result:", result)

conn.close()
server.close()
