from communication.incoming.message_event import MessageEvent
from game.users.user import User
from network.messages.client_message import ClientMessage


class PurchaseFromCatalogEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        page_id = request.pop_wired_int32()[0]
        print("page id : " + str(page_id))

        item_id = request.pop_wired_uint()[0]
        print("item id : " + str(item_id))

        extra_data = request.pop_fixed_string()
        print("extradata : " + str(extra_data))
