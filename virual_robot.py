import socket
import time

def main():
    robot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    robot_socket.connect(('0.0.0.0', 8080))

    while True:
        msg = input()
        robot_socket.send(msg.encode())
        response = robot_socket.recv(1024).decode()
        print(f"Received from server: {response}")
        time.sleep(2)

if __name__ == "__main__":
    main()

