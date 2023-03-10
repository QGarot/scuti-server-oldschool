from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.flat_created_message_composer import FlatCreatedMessageComposer
from communication.outgoing.rooms.height_map_message_composer import HeightMapMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class CreateFlatMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        room_name = request.pop_fixed_string()
        model = request.pop_fixed_string()
        print("A new room is creadted: " + room_name)
        user.send(FlatCreatedMessageComposer(1, room_name))
