from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class InitCryptoMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(src.communication.outgoing.header.InitCryptoMessageComposer)

    def get_response(self):
        pass

    def compose(self):
        # TODO: work on token
        # self.response.append_string_with_break("9875802655200380")  # token
        # self.response.append_int32(72)
        pass
