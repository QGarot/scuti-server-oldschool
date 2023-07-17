from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class ModMessageComposer(MessageComposer):
    def __init__(self, message: str, url: str = None):
        self.response = ServerMessage(161)
        self.message = message
        self.url = url

    def get_response(self) -> ServerMessage:
        return self.response

    def compose(self) -> None:
        self.response.append_string_with_break(self.message)
        if self.url is not None:
            self.response.append_string_with_break(self.url)
