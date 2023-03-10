from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class SessionParamsMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.SessionParamsMessageComposer)

    def compose(self):
        self.response.append_int32(0)

    def get_response(self):
        return self.response
