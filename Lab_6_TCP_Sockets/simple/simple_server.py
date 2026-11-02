import socket

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 60000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("TCP Server is waiting for file...")

client_socket, client_address = server_socket.accept()

# Receive filename
data = client_socket.recv(BUFFER_SIZE)
filename = data.decode()

# Receive file size
data = client_socket.recv(BUFFER_SIZE)
filesize = int(data.decode())

print("Receiving:", filename)

output_file = "received_" + filename

# Send READY
client_socket.sendall(b"READY")

received = 0

with open(output_file, "wb") as file:

    while received < filesize:

        data = client_socket.recv(BUFFER_SIZE)

        file.write(data)
        received += len(data)

        client_socket.sendall(b"ACK")

print("File received successfully!")
print("Saved as:", output_file)

client_socket.close()
server_socket.close()