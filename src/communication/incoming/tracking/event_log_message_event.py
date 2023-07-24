from src.communication.incoming.message_event import MessageEvent
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class EventLogMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        print(request.pop_fixed_string())
        print(request.pop_fixed_string())
        print(request.pop_fixed_string())
        print(request.pop_fixed_string())
        print(request.pop_int32())
