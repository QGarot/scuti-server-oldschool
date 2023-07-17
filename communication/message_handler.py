import utils.logger
from communication.incoming.catalog.get_catalog_index_event import GetCatalogIndexEvent
from communication.incoming.catalog.get_catalog_page_event import GetCatalogPageEvent
from communication.incoming.catalog.get_is_offer_giftable_event import GetIsOfferGiftableEvent
from communication.incoming.catalog.purchase_from_catalog_event import PurchaseFromCatalogEvent
from communication.incoming.handshake.info_retrieve_message_event import InfoRetrieveMessageEvent
from communication.incoming.handshake.sso_ticket_message_event import SSOTicketMessageEvent
from communication.incoming.navigator.get_official_rooms_message_event import GetOfficialRoomsMessageEvent
from communication.incoming.rooms.chat.chat_message_event import ChatMessageEvent
from communication.incoming.rooms.engine.get_furniture_aliases_message_event import GetFurnitureAliasesMessageEvent
from communication.incoming.rooms.engine.get_room_entry_data_message_composer import GetRoomEntryDataMessageEvent
from communication.incoming.navigator.my_rooms_search_message_event import MyRoomsSearchMessageEvent
from communication.incoming.rooms.session.open_flat_connection_message_event import OpenFlatConnectionMessageEvent
from communication.incoming.handshake.disconnect_message_event import DisconnectMessageEvent
from communication.incoming.inventory.purse.get_credits_info_message_event import GetCreditsInfoEvent
from communication.incoming.tracking.event_log_message_event import EventLogMessageEvent
from communication.incoming.users.scr_get_user_info_message_event import ScrGetUserInfoMessageEvent
from game.users.user import User
from communication.incoming.handshake.init_crypto_message_event import InitCryptoMessageEvent
from network.messages.client_message import ClientMessage

incoming = {
    206: InitCryptoMessageEvent(),
    415: SSOTicketMessageEvent(),
    434: MyRoomsSearchMessageEvent(),
    391: OpenFlatConnectionMessageEvent(),
    215: GetFurnitureAliasesMessageEvent(),
    390: GetRoomEntryDataMessageEvent(),
    7: InfoRetrieveMessageEvent(),
    52: ChatMessageEvent(),
    8: GetCreditsInfoEvent(),
    380: GetOfficialRoomsMessageEvent(),
    512: DisconnectMessageEvent(),
    101: GetCatalogIndexEvent(),
    102: GetCatalogPageEvent(),
    100: PurchaseFromCatalogEvent(),
    3030: GetIsOfferGiftableEvent(),
    26: ScrGetUserInfoMessageEvent(),
    482: EventLogMessageEvent()

}


def handle(user: User, header: int, client_message: ClientMessage) -> None:
    """
    Handle a client message from users connection
    :param user: client
    :param header:
    :param client_message: packet to analyse
    :return:
    """
    if header in incoming:
        utils.logger.log_packet(header, "Received!")
        incoming[header].handle(user, client_message)
    else:
        utils.logger.log_packet(header, "Packet not saved")
