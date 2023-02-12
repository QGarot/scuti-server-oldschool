from communication.outgoing.message_composer import MessageComposer


class User:
    def __init__(self, socket):
        self.socket = socket

    def send(self, server_message: MessageComposer) -> None:
        """
        Compose and send a pack to the client
        :param server_message:
        :return:
        """
        server_message.compose()
        buff = server_message.get_response().get_bytes()
        self.socket.send(bytearray(buff))
        print(type(server_message).__name__ + " sent!")
