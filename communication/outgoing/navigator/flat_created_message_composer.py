from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class FlatCreatedMessageComposer(MessageComposer):
    def __init__(self, room_id: int, room_name: str):
        self.response = ServerMessage(communication.outgoing.header.FlatCreatedMessageComposer)
        self.room_id = room_id
        self.room_name = room_name

    def compose(self):
        self.response.append_uint(self.room_id)
        self.response.append_string_with_break(self.room_name)

    def get_response(self):
        return self.response
