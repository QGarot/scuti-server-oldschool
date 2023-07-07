from communication.incoming.message_event import MessageEvent
from game.users.user import User
from network.messages.client_message import ClientMessage


class PurchaseFromCatalogEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        print("PageID: " + str(request.pop_wired_int32()))
        print("ItemID: " + str(request.pop_wired_uint()))
        print("ExtraData: " + request.pop_fixed_string())
