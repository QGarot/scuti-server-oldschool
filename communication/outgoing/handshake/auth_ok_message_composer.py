from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class AuthenticationOKMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(3)

    def compose(self):
        pass

    def get_response(self):
        return self.response
