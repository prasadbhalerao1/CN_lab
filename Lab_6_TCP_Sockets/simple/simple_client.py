import socket
import os

SERVER_IP = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 60000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

filename = input("Enter file name: ")

filesize = os.path.getsize(filename)

# Send filename
client_socket.sendall(filename.encode())

# Send file size
client_socket.sendall(str(filesize).encode())

# Receive READY
data = client_socket.recv(BUFFER_SIZE)

if data == b"READY":

    with open(filename, "rb") as file:

        while True:
            data = file.read(BUFFER_SIZE)

            if not data:
                break

            client_socket.sendall(data)

            ack = client_socket.recv(BUFFER_SIZE)

    print("File sent successfully!")

client_socket.close()