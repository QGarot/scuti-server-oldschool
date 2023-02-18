from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.height_map_message_composer import HeightMapMessageComposer, \
    FloorHeightMapMessageComposer
from communication.outgoing.rooms.room_entry_info_message_composer import RoomEntryInfoMessageComposer
from communication.outgoing.rooms.room_visualization_settings_message_composer import RoomVisualizationSettingsComposer
from communication.outgoing.rooms.users_message_composer import UsersMessageComposer
from game.rooms.models.room_model_manager import RoomModelManager
from game.rooms.room_manager import RoomManager
from game.users.user import User
from network.messages.client_message import ClientMessage


class GetRoomEntryDataMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        room = RoomManager.get_instance().get_room_by_id(user.room_id)
        model = RoomModelManager.get_instance().get_model_by_name(room.get_room_data().get_model())

        user.send(HeightMapMessageComposer(model))
        user.send(FloorHeightMapMessageComposer(model))
        user.send(UsersMessageComposer(user))

        # TODO: check rights
        user.send(RoomEntryInfoMessageComposer(room.get_room_data().is_private(), room.get_room_data().get_id(), True))
        user.send(RoomVisualizationSettingsComposer())
