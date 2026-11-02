# Experiment 6, Task 2: TCP File Transfer Server

import socket
import os

HOST = "0.0.0.0"
PORT = 5001

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder
os.makedirs("server_files", exist_ok=True)


def receive_line(conn):
    data = b""
    while True:
        ch = conn.recv(1)
        if not ch or ch == b"\n":
            break
        data += ch
    return data.decode()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if os.name != "nt":  # Lets the server restart straight away on Linux
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print("File Server is waiting...")
conn, addr = server.accept()
print("Connected by:", addr)

filename = os.path.basename(receive_line(conn))
filepath = os.path.join("server_files", filename)

if os.path.isfile(filepath):
    conn.sendall(b"OK\n")
    with open(filepath, "rb") as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            conn.sendall(data)
    print("File sent successfully!")
else:
    conn.sendall(b"ERROR: File not found\n")

conn.close()
server.close()
