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
        self.response.append_string_with_break("sh-290-64.ca-3292-63.ch-215-83.lg-275-83.hr-893-45.fa-1201-63.ha-3054"
                                               "-91-110.hd-180-1383")
        self.response.append_int32(1)
        self.response.append_int32(0)
        self.response.append_int32(23)
        self.response.append_string_with_break("2.0")
        self.response.append_int32(2)
        self.response.append_int32(1)
        self.response.append_string_with_break("M")
        self.response.append_int32(-1)
        self.response.append_int32(1)
        self.response.append_int32(-1)
        self.response.append_string_with_break("")
        self.response.append_int32(0)
