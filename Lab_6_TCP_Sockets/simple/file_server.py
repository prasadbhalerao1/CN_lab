# Experiment 6, Task 2: Simple TCP File Transfer Server

import socket
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder

HOST = "0.0.0.0"
PORT = 5001
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print("File Server is waiting...")

conn, addr = server.accept()
print("Connected by:", addr)

# Receive filename
filename = os.path.basename(conn.recv(BUFFER_SIZE).decode())
filepath = os.path.join("..", "server_files", filename)

if os.path.isfile(filepath):
    conn.sendall(b"OK")

    with open(filepath, "rb") as file:

        while True:
            data = file.read(BUFFER_SIZE)

            if not data:
                break

            conn.sendall(data)

    print("File sent successfully!")

else:
    conn.sendall(b"NO")
    print("File not found:", filename)

conn.close()
server.close()
