import socket
import threading
import time
from robot import Robot

robots = []

def listen():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 9000)) 
    server_socket.listen(5)
    print("[LISTENER]: Server listening on port 9000")

    while True:
        client_socket, addr = server_socket.accept()
        robot = Robot(client_socket, addr)
        robots.append(robot)
        print(f"[LISTENER]: Accepted connection from {addr}")
        threading.Thread(target=robot.handle_connection).start()

def main():
    threading.Thread(target=listen).start()

    while True:
        for bot in robots:
            bot.print_pos()
        print("----------")
        time.sleep(1)
if __name__ == "__main__":
    main()
