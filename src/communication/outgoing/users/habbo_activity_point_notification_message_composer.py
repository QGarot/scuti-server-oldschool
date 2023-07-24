from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class HabboActivityPointNotificationMessageComposer(MessageComposer):
    def __init__(self, point_type: int, amount: int):
        self.response = ServerMessage(src.communication.outgoing.header.HabboActivityPointNotificationMessageComposer)
        self.type = point_type
        self.amount = amount

    def compose(self):
        self.response.append_int32(self.amount)
        self.response.append_int32(0)
        self.response.append_int32(self.type)  # pixels (0), shells (4)

    def get_response(self):
        return self.response
