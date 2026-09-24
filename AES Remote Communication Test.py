import socket
import threading

def message_input(message_var):
    message = input("Input message data: ")
    message_var.sendall(message.encode())

mode_set = input("Client or Host: ")

if mode_set == "host":
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
elif mode_set.lower() == "client":
    ip_address = input("Input target IP address: ")

port = int(input("Input target port: "))
socket_bind = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if mode_set.lower() == "client":
    socket_bind.connect((ip_address, port))
    com_thread = threading.Thread(target=message_input, args=(socket_bind), daemon=True)
    com_thread.start()
    while True:
        response = socket_bind.recv(1024)
        if response:
            print(f"Received: {response.decode()}")

elif mode_set.lower() == "host":
    socket_bind.bind((ip_address, port))
    socket_bind.listen()
    print("Listening for others...")
    conn, addr = socket_bind.accept()
    com_thread = threading.Thread(target=message_input, args=(conn), daemon=True)
    com_thread.start()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if data:
                print(data.decode())
try:
    socket_bind.shutdown(socket.SHUT_RDWR)
finally:
    socket_bind.close()