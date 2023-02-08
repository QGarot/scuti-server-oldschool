from game.user.user import User
from network.messages.client_message import ClientMessage


class MessageEvent:
    @staticmethod
    def handle(user: User, request: ClientMessage):
        pass
