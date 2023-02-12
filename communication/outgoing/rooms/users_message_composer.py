import communication.outgoing.header
from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class UsersMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.UsersMessageComposer)

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_int32(1)

        self.response.append_int32(1)
        self.response.append_string_with_break("Tig3r")
        self.response.append_string_with_break("cc stp dsl")
        self.response.append_string_with_break("hr-115-42.hd-190-1.ch-215-62.lg-285-91.sh-290-62")
        self.response.append_int32(1)
        self.response.append_int32(4)
        self.response.append_int32(5)
        self.response.append_string_with_break("0.0")
        self.response.append_int32(2)
        self.response.append_int32(1)
        self.response.append_string_with_break("M")
        self.response.append_int32(-1)
        self.response.append_int32(1)
        self.response.append_int32(-1)
        self.response.append_string_with_break("")
        self.response.append_int32(0)
