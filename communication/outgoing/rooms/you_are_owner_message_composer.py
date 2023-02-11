from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class YouAreOwnerMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(47)

    def get_response(self) -> ServerMessage:
        return self.response

    def compose(self):
        pass
