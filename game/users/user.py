from communication.outgoing.message_composer import MessageComposer


class User:
    def __init__(self, socket):
        self.socket = socket

    def send(self, server_message: MessageComposer) -> None:
        server_message.compose()
        self.socket.send(bytearray(server_message.get_response().get_bytes()))
