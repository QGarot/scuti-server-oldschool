from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.open_connection_message_composer import OpenConnectionMessageComposer
from communication.outgoing.rooms.room_property_message_composer import RoomPropertyMessageComposer
from communication.outgoing.rooms.room_ready_message_composer import RoomReadyMessageComposer
from game.rooms.models.room_model_manager import RoomModelManager
from game.rooms.room_manager import RoomManager
from game.users.user import User
from network.messages.client_message import ClientMessage


class OpenFlatConnectionMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        room_id = request.pop_wired_uint()
        room = RoomManager.get_instance().get_room_by_id(room_id)
        model = RoomModelManager.get_instance().get_model_by_name(room.get_room_data().get_model())

        # Set RoomUser
        user.room_id = room_id
        user.pos_x = model.door_x
        user.pos_y = model.door_y
        user.pos_z = model.door_z

        # PrepareRoomForUser
        user.send(OpenConnectionMessageComposer(room_id, room.get_room_data().get_category()))
        user.send(RoomReadyMessageComposer(room_id, model.name))
        user.send(RoomPropertyMessageComposer())
