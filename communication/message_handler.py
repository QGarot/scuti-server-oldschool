import utils.logger
from communication.incoming.handshake.event_log_message_event import EventLogMessageEvent
from communication.incoming.handshake.sso_ticket_message_event import SSOTicketMessageEvent
from communication.incoming.rooms.can_create_room_message_event import CanCreateRoomMessageEvent
from communication.incoming.rooms.create_flat_message_event import CreateFlatMessageEvent
from communication.incoming.rooms.my_room_search_message_event import MyRoomsSearchMessageEvent
from communication.incoming.rooms.open_flat_connection_message_event import OpenFlatConnectionMessageEvent
from game.users.user import User
from communication.incoming.handshake.init_crypto_message_event import InitCryptoMessageEvent
from network.messages.client_message import ClientMessage

incoming = {
    206: InitCryptoMessageEvent(),
    415: SSOTicketMessageEvent(),
    482: EventLogMessageEvent(),
    434: MyRoomsSearchMessageEvent(),
    387: CanCreateRoomMessageEvent(),
    29: CreateFlatMessageEvent(),
    391: OpenFlatConnectionMessageEvent()
}


def handle(user: User, header: int, client_message: ClientMessage) -> None:
    """
    Handle a client message from users connection
    :param user:
    :param header:
    :param client_message:
    :return:
    """
    if header in incoming:
        utils.logger.log_packet(header, "Received!")
        incoming[header].handle(user, client_message)
    else:
        utils.logger.log_packet(header, "Packet not saved")
