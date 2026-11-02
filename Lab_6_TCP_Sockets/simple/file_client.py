# Experiment 6, Task 2: Simple TCP File Transfer Client

import socket
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder

# Usage: python file_client.py [server_ip]   (no IP = same computer)
SERVER_IP = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 5001
BUFFER_SIZE = 60000

filename = input("Enter file name: ")

filesize = os.path.getsize(filename)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

# Send filename and file size together, like: sample.txt|93
client_socket.sendall(f"{os.path.basename(filename)}|{filesize}".encode())

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
