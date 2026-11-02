# Experiment 6, Task 2: TCP File Transfer Client

import socket
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder

# Usage: python file_client.py [server_ip]   (no IP = same computer)
HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 5001


def receive_line(client):
    data = b""
    while True:
        ch = client.recv(1)
        if not ch or ch == b"\n":
            break
        data += ch
    return data.decode()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

filename = input("Enter filename: ")
client.sendall((filename + "\n").encode())

response = receive_line(client)

if response == "OK":
    output_name = "received_" + os.path.basename(filename)
    with open(output_name, "wb") as file:
        while True:
            data = client.recv(1024)
            if not data:
                break
            file.write(data)
    print("File received successfully!")
else:
    print(response)

client.close()
