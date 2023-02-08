from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class UserObjectMessageComposer(MessageComposer):

    def __init__(self):
        self.response = ServerMessage(5)

    def compose(self):
        self.response.append_string_with_break("1")
        self.response.append_string_with_break("Tig3r")
        self.response.append_string_with_break("hr-115-42.hd-195-19.ch-3030-82.lg-275-1408.fa-1201.ca-1804-64")
        self.response.append_string_with_break("M")
        self.response.append_string_with_break("")
        self.response.append_string_with_break("Tig3r")
        self.response.append_int32(0)
        self.response.append_int32(10)
        self.response.append_int32(10)
        self.response.append_int32(10)
        self.response.append_boolean(True)

    def get_response(self):
        return self.response
