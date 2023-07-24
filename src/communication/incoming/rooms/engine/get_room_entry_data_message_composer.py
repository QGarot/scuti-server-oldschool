from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.rooms.engine.height_map_message_composer import HeightMapMessageComposer, \
    FloorHeightMapMessageComposer
from src.communication.outgoing.rooms.engine.room_entry_info_message_composer import RoomEntryInfoMessageComposer
from src.communication.outgoing.rooms.engine.room_visualization_settings_message_composer import RoomVisualizationSettingsComposer
from src.communication.outgoing.rooms.engine.users_message_composer import UsersMessageComposer
from src.game.rooms.models.room_model_manager import RoomModelManager
from src.game.rooms.room_manager import RoomManager
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


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

        # Update current visitors in the room
        room.entity.append(user)
        RoomManager.get_instance().update_current_visitors_in_a_room(room.get_room_data().get_id())
