from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.catalog.catalog_index_message_composer import CatalogIndexMessageComposer
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class GetCatalogIndexEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        user.send(CatalogIndexMessageComposer())
