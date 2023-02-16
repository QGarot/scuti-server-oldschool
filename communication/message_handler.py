import utils.logger
from communication.incoming.handshake.info_retrieve_message_event import InfoRetrieveMessageEvent
from communication.incoming.handshake.sso_ticket_message_event import SSOTicketMessageEvent
from communication.incoming.rooms.chat_message_event import ChatMessageEvent
from communication.incoming.rooms.get_furniture_aliases_message_event import GetFurnitureAliasesMessageEvent
from communication.incoming.rooms.get_room_entry_data_message_composer import GetRoomEntryDataMessageEvent
from communication.incoming.rooms.my_room_search_message_event import MyRoomsSearchMessageEvent
from communication.incoming.rooms.open_flat_connection_message_event import OpenFlatConnectionMessageEvent
from communication.incoming.users.get_credits_info_message_event import GetCreditsInfoEvent
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
