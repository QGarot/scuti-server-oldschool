from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class InitCryptoMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.InitCryptoMessageComposer)

    def get_response(self):
        pass

    def compose(self):
        # TODO: work on token
        # self.response.append_string_with_break("9875802655200380")  # token
        # self.response.append_int32(72)
        pass
