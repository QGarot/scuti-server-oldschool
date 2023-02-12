import communication.outgoing.header
from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class RoomEntryInfoMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.RoomEntryInfoMessageComposer)

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_boolean(True)  # is private room
        self.response.append_int32(1)  # room id
        self.response.append_boolean(True)  # about rights
