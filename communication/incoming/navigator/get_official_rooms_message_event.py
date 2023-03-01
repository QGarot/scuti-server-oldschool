from communication.incoming.message_event import MessageEvent
from communication.outgoing.navigator.official_rooms_message_composer import OfficialRoomsMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class GetOfficialRoomsMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        user.send(OfficialRoomsMessageComposer())
