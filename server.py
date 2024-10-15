import socket
import os

def start_server():
    # Set the server parameters
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5001))  # Bind to all interfaces on port 5001
    server_socket.listen(5)  # Allow 5 connections in the queue

    print("Server is listening on port 5001...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established.")

        file_name = client_socket.recv(1024).decode()
        if not file_name:
            break

        file_size = client_socket.recv(1024).decode()

        with open(file_name, 'wb') as file:
            received_size = 0
            while received_size < int(file_size):
                bytes_read = client_socket.recv(1024)
                if not bytes_read:
                    break
                file.write(bytes_read)
                received_size += len(bytes_read)

        print(f"File '{file_name}' received successfully.")
        client_socket.close()

    server_socket.close()

if __name__ == '__main__':
    start_server()
