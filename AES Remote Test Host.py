import socket

# Local IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(local_ip)

ip_address = input("Input target IP address: ")
port = int(input("Input target port: "))

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to a specific address and port
server.bind((ip_address, port))

# Listen for incoming connections
server.listen()
print("Server is listening...")

# Accept a connection
conn, addr = server.accept()
with conn:
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)  # Echo back