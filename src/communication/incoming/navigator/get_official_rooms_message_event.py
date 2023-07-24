from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.navigator.official_rooms_message_composer import OfficialRoomsMessageComposer
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class GetOfficialRoomsMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        user.send(OfficialRoomsMessageComposer())
