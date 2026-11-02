# Experiment 5: Simple UDP File Transfer Server

import socket
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("UDP Server is waiting for file...")

# Receive filename
data, client_address = server_socket.recvfrom(BUFFER_SIZE)
filename = os.path.basename(data.decode())

# Receive file size
data, client_address = server_socket.recvfrom(BUFFER_SIZE)
filesize = int(data.decode())

print("Receiving:", filename)

output_file = "received_" + filename

# Send READY
server_socket.sendto(b"READY", client_address)

received = 0

with open(output_file, "wb") as file:

    while received < filesize:

        data, client_address = server_socket.recvfrom(BUFFER_SIZE)

        file.write(data)
        received += len(data)

        server_socket.sendto(b"ACK", client_address)

print("File received successfully!")
print("Saved as:", output_file)

server_socket.close()
