from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.catalog.is_offer_giftable_message_composer import IsOfferGiftableMessageComposer
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class GetIsOfferGiftableEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        item_id = request.pop_wired_uint()
        user.send(IsOfferGiftableMessageComposer(item_id))
