import socket
from threading import *

filepath = "/home/andrew/SFhack/python/temp.txt"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.3.5.59"
port = 8081
print(host)
print(port)
serversocket.bind((host, port))


keyWords = ["claim", "auto", "car", "vehicle", "rental", "quote", "home",
            "house", "fire", "life", "status"]


class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            out = []
            msg = self.sock.recv(1024).decode()
            # print(msg)
            print('Client sent:', msg)
            for thing in keyWords:
                if thing in msg.replace("auto", "car").replace("vehicle", "car").replace("home", "house"):
                    out.append(thing)

            print(out)
            y = ",".join(map(str, out))
            with open(filepath, 'w') as f:
                f.truncate()
                f.write(y)
                f.close()

            if str(msg) == str("stop"):
                serversocket.close()
                break
            self.sock.send(b'\nServer Recived Msg\n')

serversocket.listen(5)
print('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
