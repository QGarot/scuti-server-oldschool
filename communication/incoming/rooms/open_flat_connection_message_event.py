from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.client_private_room_message_composer import ClientPrivateRoomMessageComposer
from communication.outgoing.rooms.height_map_message_composer import HeightMapMessageComposer, \
    FloorHeightMapMessageComposer
from communication.outgoing.rooms.room_property_message_composer import RoomPropertyMessageComposer
from communication.outgoing.rooms.you_are_owner_message_composer import YouAreOwnerMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


def prepare_room_for_user(user: User, room_id):
    user.send(ClientPrivateRoomMessageComposer(room_id))


def load_room_for_user(user: User):
    print("OPENFLAT3")
    # wallpaper, floor, landscape
    user.send(RoomPropertyMessageComposer())
    print("OPENFLAT4")
    # check rights
    user.send(YouAreOwnerMessageComposer())
    print("OPENFLAT5")


class OpenFlatConnectionMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        room_id = request.pop_wired_uint()

        user.send(ClientPrivateRoomMessageComposer(room_id))

        # wallpaper, floor, landscape
        user.send(RoomPropertyMessageComposer())
        # check rights
        user.send(YouAreOwnerMessageComposer())
        # Heightmap
        user.send(HeightMapMessageComposer())
        # Floor
        user.send(FloorHeightMapMessageComposer())
