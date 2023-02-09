from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class AuthenticationOKMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.AuthenticationOKMessageComposer)

    def compose(self):
        pass

    def get_response(self):
        return self.response
