from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.guest_room_search_result_message_composer import GuestRoomSearchResultMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class MyRoomsSearchMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(GuestRoomSearchResultMessageComposer(user.get_details().get_username()))
