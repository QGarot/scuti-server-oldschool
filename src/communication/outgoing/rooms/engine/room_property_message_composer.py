from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class RoomPropertyMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(src.communication.outgoing.header.RoomPropertyMessageComposer)

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_string_with_break("landscape")
        self.response.append_string_with_break("0.0")
