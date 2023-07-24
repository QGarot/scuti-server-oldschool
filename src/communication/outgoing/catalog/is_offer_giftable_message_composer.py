from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage

# TODO: fix gift
class IsOfferGiftableMessageComposer(MessageComposer):
    def __init__(self, item_id: int):
        self.response = ServerMessage(622)
        self.item_id = item_id

    def compose(self) -> None:
        self.response.append_uint(self.item_id)
        self.response.append_boolean(False)

    def get_response(self) -> ServerMessage:
        return self.response
