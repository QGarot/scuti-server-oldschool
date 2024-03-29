from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage


class HabboBroadcastMessageComposer(MessageComposer):
    def __init__(self, message: str):
        self.response = ServerMessage(139)
        self.message = message

    def get_response(self) -> ServerMessage:
        return self.response

    def compose(self) -> None:
        self.response.append_string_with_break(self.message)
