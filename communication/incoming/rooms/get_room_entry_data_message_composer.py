from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.height_map_message_composer import HeightMapMessageComposer, \
    FloorHeightMapMessageComposer
from communication.outgoing.rooms.room_entry_info_message_composer import RoomEntryInfoMessageComposer
from communication.outgoing.rooms.room_visualization_settings_message_composer import RoomVisualizationSettingsComposer
from communication.outgoing.rooms.users_message_composer import UsersMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class GetRoomEntryDataMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(HeightMapMessageComposer())
        user.send(FloorHeightMapMessageComposer())
        user.send(UsersMessageComposer(user.get_details()))
        user.send(RoomEntryInfoMessageComposer())
        user.send(RoomVisualizationSettingsComposer())
