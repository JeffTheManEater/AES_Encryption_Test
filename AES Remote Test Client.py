import socket

ip_address = input("Input target IP address: ")
port = int(input("Input target port: "))

# Create a socket and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_address, port))

# Send and receive data
client.sendall(b"Hello, Server!")
response = client.recv(1024)
print(f"Received: {response.decode()}")

client.close()