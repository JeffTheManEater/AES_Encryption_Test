import socket
import threading

def message_output_host(message_var, message_addr):
    with message_var:
        print(f"Connected by {message_addr}")
        while True:
            data = message_var.recv(1024)
            if data:
                print(data.decode())

def message_output_client(message_var):
    while True:
        response = message_var.recv(1024)
        if response:
            print(f"Received: {response.decode()}")

mode_set = input("Client or Host: ")

if mode_set.lower() == "client":
    ip_address = input("Input target IP address: ")
elif mode_set == "host":
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

port = int(input("Input target port: "))
socket_bind = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if mode_set.lower() == "client":
    socket_bind.connect((ip_address, 
                         port))
    com_thread = threading.Thread(target=message_output_client, 
                                  args=(socket_bind), 
                                  daemon=True)
    com_thread.start()
    while True:
        message = input("Input message data: ")
        socket_bind.sendall(message.encode())

elif mode_set.lower() == "host":
    socket_bind.bind((ip_address, 
                      port))
    socket_bind.listen()
    print("Listening for others...")
    conn, addr = socket_bind.accept()
    com_thread = threading.Thread(target=message_output_host, 
                                  args=(conn, addr), 
                                  daemon=True)
    com_thread.start()
    while True:
        message = input("\nInput message data: ")
        conn.sendall(message.encode())
    
try:
    socket_bind.shutdown(socket.SHUT_RDWR)
finally:
    socket_bind.close()