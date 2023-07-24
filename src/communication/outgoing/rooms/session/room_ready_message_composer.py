from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class RoomReadyMessageComposer(MessageComposer):
    def __init__(self, room_id: int, room_model: str):
        self.response = ServerMessage(src.communication.outgoing.header.RoomReadyMessageComposer)
        self.room_id = room_id
        self.room_model = room_model

    def compose(self):
        self.response.append_string_with_break(self.room_model)
        self.response.append_int32(self.room_id)  # room id

    def get_response(self):
        return self.response
