from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class FlatCreatedMessageComposer(MessageComposer):
    def __init__(self, room_id: int, room_name: str):
        self.response = ServerMessage(src.communication.outgoing.header.FlatCreatedMessageComposer)
        self.room_id = room_id
        self.room_name = room_name

    def compose(self):
        self.response.append_uint(self.room_id)
        self.response.append_string_with_break(self.room_name)

    def get_response(self):
        return self.response
