import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('localhost', 8080))
server_socket.listen()


while True:
    print(("Before access"))
    client_socket, addr = server_socket.accept()
    print('Connected by', addr)
    while True:
        print("before receiving")
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            resource = 'hello world\n'.encode()
            client_socket.sendall(resource)
    print("Outside inner loop")
    client_socket.close()