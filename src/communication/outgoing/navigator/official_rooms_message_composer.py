from src.communication.outgoing.message_composer import MessageComposer
from src.game.navigator.navigator_manager import NavigatorManager
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class OfficialRoomsMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(src.communication.outgoing.header.OfficialRoomsMessageComposer)
        self.rooms = NavigatorManager.get_instance().get_public_rooms()

    def get_response(self) -> ServerMessage:
        return self.response

    def compose(self) -> None:
        self.response.append_int32(len(self.rooms))
        for room in self.rooms:
            self.response.append_int32(room.get_id())
            self.response.append_string_with_break(room.get_caption())  # Public room name
            self.response.append_string_with_break("")  # Description
            self.response.append_uint(room.get_type())  # Type
            self.response.append_string_with_break(room.get_caption())  # Room name
            self.response.append_string_with_break(room.get_description())  # Description
            self.response.append_int32(room.get_recommended())
            self.response.append_int32(0)
            self.response.append_int32(3)
            self.response.append_string_with_break("")
            self.response.append_uint(1337)
            self.response.append_boolean(True)
            self.response.append_string_with_break("")
            self.response.append_int32(50)  # users max
            self.response.append_uint(room.get_room_id())  # Room id
