from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.users.user_object_message_composer import UserObjectMessageComposer
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class InfoRetrieveMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        user.send(UserObjectMessageComposer(user.get_details()))
