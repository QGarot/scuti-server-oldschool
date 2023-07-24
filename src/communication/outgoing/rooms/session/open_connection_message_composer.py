from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class OpenConnectionMessageComposer(MessageComposer):
    def __init__(self, room_id, room_category_id):
        self.response = ServerMessage(src.communication.outgoing.header.OpenConnectionMessageComposer)
        self.room_id = room_id
        self.room_category_id = room_category_id

    def compose(self):
        self.response.append_int32(self.room_id)
        self.response.append_int32(self.room_category_id)

    def get_response(self):
        return self.response
