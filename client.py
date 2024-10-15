import socket
import os
from tkinter import Tk, Button, filedialog, Label


def select_file_and_send():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename()

    if file_path:
        send_file(file_path)


def send_file(file_path):
    # Set the client parameters
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5001))  # Connect to the server

    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    # Send file details (name and size)
    client_socket.send(file_name.encode())
    client_socket.send(str(file_size).encode())

    # Send the file content
    with open(file_path, 'rb') as file:
        while True:
            bytes_read = file.read(1024)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)

    print(f"File '{file_name}' sent successfully.")
    client_socket.close()


def create_gui():
    # Create a simple GUI for file selection
    root = Tk()
    root.title("File Transfer Client")

    label = Label(root, text="Select a file to send")
    label.pack(pady=10)

    send_button = Button(root, text="Select File", command=select_file_and_send)
    send_button.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    create_gui()
