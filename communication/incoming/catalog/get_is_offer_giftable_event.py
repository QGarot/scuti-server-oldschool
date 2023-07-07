from communication.incoming.message_event import MessageEvent
from communication.outgoing.catalog.is_offer_giftable_message_composer import IsOfferGiftableMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class GetIsOfferGiftableEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        item_id = request.pop_wired_uint()
        user.send(IsOfferGiftableMessageComposer(item_id))
