from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class CanCreateRoomMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(src.communication.outgoing.header.CanCreateRoomMessageComposer)

    def compose(self):
        self.response.append_int32(0)
        self.response.append_int32(1)

    def get_response(self):
        return self.response
