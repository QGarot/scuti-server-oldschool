from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.GuestRoomSearchResultMessageComposer import GuestRoomSearchResultMessageComposer
from game.user.user import User
from network.messages.client_message import ClientMessage


class MyRoomsSearchMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(GuestRoomSearchResultMessageComposer())
