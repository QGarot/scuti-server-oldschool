from src.communication.incoming.message_event import MessageEvent
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage
from src.game.users.user_manager import UserManager


class DisconnectMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        # print(UserManager.get_instance().get_users())
        # print(UserManager.get_instance().get_connections())
        UserManager.get_instance().disconnect(user)
        # print(UserManager.get_instance().get_users())
        # print(UserManager.get_instance().get_connections())
