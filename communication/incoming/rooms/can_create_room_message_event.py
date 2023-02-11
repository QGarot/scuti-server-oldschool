from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.can_create_room_message_composer import CanCreateRoomMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class CanCreateRoomMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(CanCreateRoomMessageComposer())
