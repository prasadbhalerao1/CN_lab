# Experiment 5: UDP File Transfer Server

import socket
import os

HOST = "0.0.0.0"
PORT = 5000
SAVE_DIR = "received_files"

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Works from any folder
os.makedirs(SAVE_DIR, exist_ok=True)


def receive(server):
    while True:
        try:
            return server.recvfrom(2048)
        except ConnectionResetError:
            # Windows reports a client that has gone away; keep serving.
            continue


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    print("UDP Server is waiting for files...")

    while True:
        data, addr = receive(server)

        if data == b"END":
            server.sendto(b"DONE", addr)
            continue

        if not data.startswith(b"FILE|"):
            continue

        try:
            _, filename, size = data.decode().split("|", 2)
            size = int(size)
            filename = os.path.basename(filename)
            if not filename or size < 0:
                continue
        except (ValueError, UnicodeDecodeError):
            continue

        filepath = os.path.join(SAVE_DIR, filename)
        print("\nReceiving:", filename)
        server.sendto(b"READY", addr)

        received = 0
        expected = 0

        with open(filepath, "wb") as file:
            while received < size:
                packet, client_addr = receive(server)

                if client_addr != addr:
                    continue

                if packet.startswith(b"FILE|"):
                    server.sendto(b"READY", addr)
                    continue

                if len(packet) < 4:
                    continue

                seq = int.from_bytes(packet[:4], "big")
                chunk = packet[4:]

                if seq == expected:
                    chunk = chunk[:size - received]
                    file.write(chunk)
                    received += len(chunk)
                    server.sendto(seq.to_bytes(4, "big"), addr)
                    expected += 1
                elif seq < expected:
                    # Duplicate packet: acknowledge again without writing twice.
                    server.sendto(seq.to_bytes(4, "big"), addr)

        last_seq = expected - 1

        while True:
            packet, client_addr = receive(server)

            if client_addr != addr:
                continue

            if packet == b"END":
                server.sendto(b"DONE", addr)
                break
            elif packet.startswith(b"FILE|"):
                server.sendto(b"READY", addr)
            elif len(packet) >= 4:
                seq = int.from_bytes(packet[:4], "big")
                if seq == last_seq:
                    server.sendto(seq.to_bytes(4, "big"), addr)

        print("File received successfully:", filename)
        print("Saved inside:", SAVE_DIR)
