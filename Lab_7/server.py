# Experiment 7: SSL/TLS Secure Server

import socket
import ssl
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder

HOST = "0.0.0.0"
PORT = 8443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("server.crt", "server.key")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if os.name != "nt":  # Lets the server restart straight away on Linux
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print("Secure Server is listening...")

secure_server = context.wrap_socket(server, server_side=True)

while True:
    try:
        conn, addr = secure_server.accept()
    except OSError as error:
        # A failed TLS handshake (e.g. a plain TCP client) must not stop the server.
        print("\nRejected connection:", error)
        continue

    print("\nConnected by:", addr)
    print("TLS Version:", conn.version())

    message = conn.recv(1024).decode()
    print("Client:", message)

    conn.sendall("Secure message received!".encode())
    conn.close()
