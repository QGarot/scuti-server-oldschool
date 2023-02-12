from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.open_connection_message_composer import OpenConnectionMessageComposer
from communication.outgoing.rooms.room_property_message_composer import RoomPropertyMessageComposer
from communication.outgoing.rooms.room_ready_message_composer import RoomReadyMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class OpenFlatConnectionMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        room_id = request.pop_wired_uint()[0]
        print(room_id)

        # PrepareRoomForUser
        user.send(OpenConnectionMessageComposer(room_id, 1))
        user.send(RoomReadyMessageComposer(room_id, "model_a"))
        user.send(RoomPropertyMessageComposer())
