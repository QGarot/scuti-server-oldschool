from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.navigator.flat_created_message_composer import FlatCreatedMessageComposer
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class CreateFlatMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        room_name = request.pop_fixed_string()
        model = request.pop_fixed_string()
        print("A new room is creadted: " + room_name)
        user.send(FlatCreatedMessageComposer(1, room_name))
