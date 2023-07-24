from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class AuthenticationOKMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(src.communication.outgoing.header.AuthenticationOKMessageComposer)

    def compose(self):
        pass

    def get_response(self):
        return self.response
