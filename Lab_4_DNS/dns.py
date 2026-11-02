# Experiment 4: DNS Lookup

import socket

print("1. Domain Name to IP Address")
print("2. IP Address to Domain Name")

choice = int(input("Enter your choice: "))

if choice == 1:
    domain = input("Enter domain name: ")

    try:
        ip = socket.gethostbyname(domain)
        print("IP Address:", ip)
    except socket.gaierror:
        print("Domain name not found!")

elif choice == 2:
    ip = input("Enter IP address: ")

    try:
        hostname = socket.gethostbyaddr(ip)
        print("Domain Name:", hostname[0])
    except (socket.herror, socket.gaierror):
        print("IP address not found!")

else:
    print("Invalid choice!")
