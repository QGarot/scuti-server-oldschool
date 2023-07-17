from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class CanCreateRoomMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.CanCreateRoomMessageComposer)

    def compose(self):
        self.response.append_int32(0)
        self.response.append_int32(1)

    def get_response(self):
        return self.response
