# Experiment 5: Simple UDP File Transfer Client

import socket
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder

# Usage: python client.py [server_ip]   (no IP = same computer)
SERVER_IP = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (SERVER_IP, PORT)

filename = input("Enter file name: ")

filesize = os.path.getsize(filename)

# Send filename
client_socket.sendto(os.path.basename(filename).encode(), server_address)

# Send file size
client_socket.sendto(str(filesize).encode(), server_address)

# Wait for READY
data, addr = client_socket.recvfrom(BUFFER_SIZE)

if data == b"READY":

    with open(filename, "rb") as file:

        while True:
            data = file.read(BUFFER_SIZE)

            if not data:
                break

            client_socket.sendto(data, server_address)

            ack, addr = client_socket.recvfrom(BUFFER_SIZE)

    print("File sent successfully!")

client_socket.close()
