# Experiment 6, Task 2: Simple TCP File Transfer Client

import socket
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder

# Usage: python file_client.py [server_ip]   (no IP = same computer)
HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 5001
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

filename = input("Enter file name: ")
client.sendall(filename.encode())

# Server replies OK or NO first
status = client.recv(2)

if status == b"OK":

    with open("received_" + filename, "wb") as file:

        while True:
            data = client.recv(BUFFER_SIZE)

            if not data:
                break

            file.write(data)

    print("File received successfully!")

else:
    print("File not found on server!")

client.close()
