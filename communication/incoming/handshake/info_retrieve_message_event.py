from communication.incoming.message_event import MessageEvent
from communication.outgoing.users.user_object_message_composer import UserObjectMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class InfoRetrieveMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        user.send(UserObjectMessageComposer())
