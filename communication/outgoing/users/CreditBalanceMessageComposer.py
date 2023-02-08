from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class CreditBalanceMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(6)

    def compose(self):
        self.response.append_string_with_break("100")

    def get_response(self):
        return self.response
