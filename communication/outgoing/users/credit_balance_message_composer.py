from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class CreditBalanceMessageComposer(MessageComposer):
    def __init__(self, credits: int):
        self.response = ServerMessage(communication.outgoing.header.CreditBalanceMessageComposer)
        self.credits = credits

    def compose(self):
        self.response.append_string_with_break(str(self.credits))

    def get_response(self):
        return self.response
