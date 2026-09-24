import socket

# Local IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

port = int(input("Input target port: "))

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to a specific address and port
server.bind((local_ip, port))

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
<<<<<<< HEAD:Remote Test/AES Remote Test Host.py
        conn.sendall(data)  # Echo back
=======
        print(data.decode())
        conn.sendall(data)  # Echo back
>>>>>>> 8e12803 (two computers can now communicate but not actually.):AES Remote Test Host.py
