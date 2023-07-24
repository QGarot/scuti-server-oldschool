from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.navigator.can_create_room_message_composer import CanCreateRoomMessageComposer
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class CanCreateRoomMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(CanCreateRoomMessageComposer())
