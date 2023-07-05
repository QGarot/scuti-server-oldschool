from communication.incoming.message_event import MessageEvent
from communication.outgoing.catalog.catalog_page_message_composer import CatalogPageMessageComposer
from communication.outgoing.catalog.habbo_club_offers_message_composer import HabboClubOffersMessageComposer
from game.catalog.catalog_manager import CatalogManager
from game.users.user import User
from network.messages.client_message import ClientMessage


class GetCatalogPageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        page_id = request.pop_wired_int32()[0]
        page = CatalogManager.get_instance().get_catalog_page_by_id(page_id)

        user.send(CatalogPageMessageComposer(page))
        if page.get_layout() == "club_buy":
            user.send(HabboClubOffersMessageComposer())
        elif page.get_layout() == "recycler":
            pass
        else:
            pass
