# Experiment 6, Task 3: Simple TCP Calculator Server

import socket

HOST = "0.0.0.0"
PORT = 5002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print("Calculator Server is waiting...")

conn, addr = server.accept()
print("Connected by:", addr)

# Receive something like: 7 + 5
num1, operator, num2 = conn.recv(1024).decode().split()
num1 = float(num1)
num2 = float(num2)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/" and num2 != 0:
    result = num1 / num2
else:
    result = "Invalid operation!"

conn.sendall(str(result).encode())
print("Result:", result)

conn.close()
server.close()
