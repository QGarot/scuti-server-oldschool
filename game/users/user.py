from communication.outgoing.message_composer import MessageComposer
from game.users.user_details import UserDetails


class User:
    def __init__(self, socket):
        self.socket = socket
        self.details = UserDetails()

    def send(self, server_message: MessageComposer) -> None:
        """
        Compose and send a pack to the client
        :param server_message:
        :return:
        """
        server_message.compose()
        self.socket.send(bytearray(server_message.get_response().get_bytes()))
        print(type(server_message).__name__ + " sent!")

    def login(self):
        print(self.get_details().get_username() + " is connected!")

    def disconnect(self) -> None:
        """
        Disconnect user from the client
        :return:
        """
        # self.socket.close()
        # TODO: fix "OSError: [WinError 10038]" when socket is closed!
        pass

    def get_details(self) -> UserDetails:
        """
        :return: user details
        """
        return self.details
