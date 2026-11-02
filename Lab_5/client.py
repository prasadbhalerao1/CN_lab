# Experiment 5: UDP File Transfer Client

import socket
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder

# Usage: python client.py [server_ip]   (no IP = same computer)
SERVER_IP = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024
TIMEOUT = 1
MAX_RETRIES = 5


def send_and_wait(client, packet, expected, server_addr):
    for attempt in range(MAX_RETRIES):
        client.sendto(packet, server_addr)

        try:
            response, addr = client.recvfrom(2048)
            if addr == server_addr and response == expected:
                return True
        except (socket.timeout, ConnectionResetError):
            print("Timeout! Retrying...")

    return False


file_types = ["script", "text", "audio", "video"]
files = []

for file_type in file_types:
    filename = input(f"Enter {file_type} file path: ")
    if not os.path.isfile(filename):
        print("File not found:", filename)
        raise SystemExit
    files.append(filename)

server_addr = (SERVER_IP, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.settimeout(TIMEOUT)

    for filename in files:
        size = os.path.getsize(filename)
        name = os.path.basename(filename)
        info = f"FILE|{name}|{size}".encode()

        if not send_and_wait(client, info, b"READY", server_addr):
            print("Server not responding!")
            raise SystemExit

        print("\nSending:", name)

        with open(filename, "rb") as file:
            seq = 0

            while True:
                chunk = file.read(BUFFER_SIZE)
                if not chunk:
                    break

                packet = seq.to_bytes(4, "big") + chunk
                ack = seq.to_bytes(4, "big")

                if not send_and_wait(client, packet, ack, server_addr):
                    print("File transfer failed!")
                    raise SystemExit

                seq += 1

        if not send_and_wait(client, b"END", b"DONE", server_addr):
            print("Completion acknowledgement not received!")
            raise SystemExit

        print("File sent successfully:", name)

print("\nAll four files transferred successfully!")
