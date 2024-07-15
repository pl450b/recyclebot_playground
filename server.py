import socket
import threading

def handle_robot_connection(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Received from robot: {message}")
        client_socket.send("We gotchya homie!".encode())

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(5)
    print("Server listening on port 8080")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        threading.Thread(target=handle_robot_connection, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
