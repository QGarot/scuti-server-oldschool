from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class UserObjectMessageComposer(MessageComposer):

    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.UserObjectMessageComposer)

    def compose(self):
        self.response.append_string_with_break("1")
        self.response.append_string_with_break("Tig3r")
        self.response.append_string_with_break("hr-115-42.hd-190-1.ch-215-62.lg-285-91.sh-290-62")
        self.response.append_string_with_break("M")
        self.response.append_string_with_break("cc dsl")
        self.response.append_string_with_break("Tig3r")
        self.response.append_boolean(False)
        self.response.append_int32(10)
        self.response.append_int32(10)
        self.response.append_int32(10)
        self.response.append_boolean(False)

    def get_response(self):
        return self.response
