from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class IgnoredUsersMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(src.communication.outgoing.header.IgnoredUsersMessageComposer)

    def get_response(self):
        return self.response

    def compose(self):
        pass
