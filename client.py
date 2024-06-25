import socket, _thread

HOST = "127.0.0.1"
PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)
        print("recive : ", repr(data.decode()))

_thread.start_new_thread(recv_data, (client_socket,))
print(">> Connect Server")

while True:
    message = input("")
    if message == "quit":
        close_data = message
        brea
    client_socket.send(message.encode())
client_socket.close()