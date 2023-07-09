from communication.incoming.message_event import MessageEvent
from communication.outgoing.users.scr_send_user_info_message_composer import ScrSendUserInfoMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class ScrGetUserInfoMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        text = request.pop_fixed_string()

        if user.get_subscription().is_valid():
            user.send(ScrSendUserInfoMessageComposer(user.get_subscription()))
