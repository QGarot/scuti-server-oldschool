from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class CanCreateRoomMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(int(0x0200))

    def compose(self):
        self.response.append_int32(0)
        self.response.append_int32(5000)

    def get_response(self):
        return self.response
