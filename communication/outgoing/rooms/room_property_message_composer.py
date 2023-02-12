import communication.outgoing.header
from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class RoomPropertyMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.RoomPropertyMessageComposer)

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_string_with_break("landscape")
        self.response.append_string_with_break("0.0")
