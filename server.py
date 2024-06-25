import socket, _thread

client_sockets = [] # 클라이언트 리스트

HOST = "127.0.0.1"
PORT = 8085

print(">> 서버 시작")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

def threaded(client_socket, addr):
    print(">> 연결된 클라이언트 : ", addr[0], ":", addr[1])

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print(">> 연결 해제된 클라이언트 : " + addr[0], ":", addr[1])
                break

            print(">> 받은 데이터 : " + addr[0], ":", addr[1], data.decode())
            for client in client_sockets:
                if client != client_socket:
                    # 클라이언트에게 데이터 전송
                    client.send(data)
        except ConnectionResetError as e:
            print(">> 연결 해제된 클라이언트 : " + addr[0], ":", addr[1])
            break
    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print("클라이언트 목록 삭제 : ", len(client_sockets))

    client_socket.close()

try:
    while True:
        print(">> 서버 대기중..")

        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        _thread.start_new_thread(threaded, (client_socket, addr))
        print("클라이언트 수 : ", len(client_sockets))

except Exception as e:
    print("에러가 발생했습니다.", e)

finally:
    server_socket.close()