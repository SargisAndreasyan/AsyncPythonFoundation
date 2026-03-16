import socket
import selectors

selector = selectors.DefaultSelector()

def server():
    # Initialize the server socket using IPv4 and TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow immediate reuse of the port after stopping the script
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8080))
    server_socket.listen()
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connections)

def accept_connections(serv_soc):
    """Handles a new incoming client connection."""
    client_socket, addr = serv_soc.accept()
    print(f"New connection from {addr}")

    # Instead, we just add the new client socket to the monitor list.
    # The event loop will call send_message() when this specific client sends data later.


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
        client_socket.close()


def event_loop():
    """Main loop that uses select() to wait for socket activity."""
    while True:
        ...


if __name__ == '__main__':
    print("Server started on localhost:8080...")
    # Note: server_socket is already in the to_monitor list defined at the top.
    event_loop()
