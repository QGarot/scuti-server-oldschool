import utils.logger
from communication.incoming.handshake.EventLogMessageEvent import EventLogMessageEvent
from communication.incoming.handshake.SSOTicketMessageEvent import SSOTicketMessageEvent
from communication.incoming.rooms.CanCreateRoomMessageEvent import CanCreateRoomMessageEvent
from communication.incoming.rooms.MyRoomsSearchMessageEvent import MyRoomsSearchMessageEvent
from game.user.user import User
from communication.incoming.handshake.InitCryptoMessageEvent import InitCryptoMessageEvent
from network.messages.client_message import ClientMessage

incoming = {
    206: InitCryptoMessageEvent(),
    415: SSOTicketMessageEvent(),
    482: EventLogMessageEvent(),
    434: MyRoomsSearchMessageEvent(),
    387: CanCreateRoomMessageEvent()
}


def handle(user: User, header: int, client_message: ClientMessage) -> None:
    """
    Handle a client message from user connection
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
