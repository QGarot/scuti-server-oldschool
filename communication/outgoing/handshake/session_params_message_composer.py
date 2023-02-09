from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class SessionParamsMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.SessionParamsMessageComposer)

    def compose(self):
        self.response.append_int32(9)
        self.response.append_int32(0)
        self.response.append_int32(0)
        self.response.append_int32(1)
        self.response.append_int32(1)
        self.response.append_int32(3)
        self.response.append_int32(0)
        self.response.append_int32(2)
        self.response.append_int32(1)
        self.response.append_int32(4)
        self.response.append_int32(1)
        self.response.append_int32(5)
        self.response.append_string_with_break("dd-MM-yyyy")
        self.response.append_int32(7)
        self.response.append_boolean(False)
        self.response.append_int32(8)
        self.response.append_string_with_break("/client")
        self.response.append_int32(9)
        self.response.append_boolean(False)

    def get_response(self):
        return self.response
