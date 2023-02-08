from communication.incoming.message_event import MessageEvent
from game.user.user import User
from network.messages.client_message import ClientMessage


class SSOTicketMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        print(request.pop_fixed_string())
