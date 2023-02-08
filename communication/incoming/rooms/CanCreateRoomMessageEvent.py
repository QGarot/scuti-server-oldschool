from communication.incoming.message_event import MessageEvent
from communication.outgoing.rooms.CanCreateRoomMessageComposer import CanCreateRoomMessageComposer
from game.user.user import User
from network.messages.client_message import ClientMessage


class CanCreateRoomMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(CanCreateRoomMessageComposer())
