import socket
from select import select

# Initialize the server socket using IPv4 and TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Allow immediate reuse of the port after stopping the script
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('localhost', 8080))
server_socket.listen()

# List of sockets to monitor for incoming data/connections.
# We must start by monitoring the server socket itself.
to_monitor = [server_socket]


def accept_connections(serv_soc):
    """Handles a new incoming client connection."""
    client_socket, addr = serv_soc.accept()
    print(f"New connection from {addr}")

    # Instead, we just add the new client socket to the monitor list.
    # The event loop will call send_message() when this specific client sends data later.
    to_monitor.append(client_socket)


def send_message(client_socket):
    """Reads data from an existing client socket and sends a response."""
    # We need try/except block to handle abrupt disconnections
    request = client_socket.recv(4096)
    if request:
        # If we received data, send the response back
        response = f'Hello world!\n'.encode()
        client_socket.send(response)
    else:
        # If recv() returns empty bytes, it means the client closed the connection gracefully.
        # We must remove it from the monitor list, otherwise select() will crash trying to read a closed socket.
        print("Client closed connection normally.")
        to_monitor.remove(client_socket)
        client_socket.close()


def event_loop():
    """Main loop that uses select() to wait for socket activity."""
    while True:
        # select() blocks execution until one of the sockets in 'to_monitor' is ready to be read.
        # It returns the list 'ready_to_read' containing only the active sockets.
        ready_to_read, _, _ = select(to_monitor, [], [])

        for sock in ready_to_read:
            if sock is server_socket:
                # If the 'server_socket' is ready, it means a new client wants to connect.
                accept_connections(sock)
            else:
                # If any other socket is ready, it means an existing client sent data.
                send_message(sock)


if __name__ == '__main__':
    print("Server started on localhost:8080...")
    # Note: server_socket is already in the to_monitor list defined at the top.
    event_loop()
