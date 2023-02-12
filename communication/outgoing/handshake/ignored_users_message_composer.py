from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class IgnoredUsersMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.IgnoredUsersMessageComposer)

    def get_response(self):
        return self.response

    def compose(self):
        pass
