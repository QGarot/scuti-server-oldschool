import communication.outgoing.header
from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class YouAreOwnerMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.YouAreOwnerMessageComposer)

    def get_response(self):
        return self.response

    def compose(self):
        pass
