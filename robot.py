import socket

class Robot:
    def __init__(self, socket_connection, address):
        self.socket_connection = socket_connection
        self.address = address
        self.pos = [1,1]
        self.dir = 0
        self.direction = 'V'

    def handle_connection(self):
        while True:
            message = self.socket_connection.recv(1024).decode()
            if not message:
                break
            if(message == 'w'):
                self.pos[1] += 1
                self.dir = 0
            elif(message == 's'):
                self.pos[1] -= 1
                self.dir = 2
            elif(message == 'a'):
                self.pos[0] -= 1
                self.dir = 3
            elif(message == 'd'):
                self.pos[0] += 1
                self.dir = 1
            else:
                self.socket_connection.send("Only send wasd commands")

    
    def print_pos(self):
        print(self.pos)
    
    def __del__(self):
        self.socket_connection.close()