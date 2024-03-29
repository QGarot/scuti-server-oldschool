from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.navigator.guest_room_search_result_message_composer import GuestRoomSearchResultMessageComposer
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class MyRoomsSearchMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(GuestRoomSearchResultMessageComposer(user.get_details().get_username()))
