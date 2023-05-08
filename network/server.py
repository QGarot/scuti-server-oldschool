import asyncore
import threading
from asyncore import dispatcher
import socket
from network.connexion import Connection


class Server(dispatcher):
    def __init__(self, host, port):
        super().__init__()
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(1)

        self.handler = None
        loop_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop")
        loop_thread.start()

    def handle_accepted(self, sock, addr):
        print("New connection from " + str(addr[0]))
        self.handler = Connection(sock)
        self.handler.new_session()
