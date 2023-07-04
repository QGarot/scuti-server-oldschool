from communication.incoming.message_event import MessageEvent
from communication.outgoing.catalog.catalog_page_message_composer import CatalogPageMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class GetCatalogPageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        page_id = request.pop_wired_int32()[0]
        user.send(CatalogPageMessageComposer(page_id))
