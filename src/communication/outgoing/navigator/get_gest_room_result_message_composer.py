from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class GetGuestRoomResultMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(src.communication.outgoing.header.GetGuestRoomResultMessageEvent)

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_boolean(True)  # is private room
        self.response.append_int32(1)  # room id
        self.response.append_boolean(True)  # about rights
