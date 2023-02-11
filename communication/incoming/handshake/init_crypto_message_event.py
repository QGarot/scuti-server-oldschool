from communication.incoming.message_event import MessageEvent
from communication.outgoing.handshake.auth_ok_message_composer import AuthenticationOKMessageComposer
from communication.outgoing.users.credit_balance_message_composer import CreditBalanceMessageComposer
from communication.outgoing.users.motd_notification_message_composer import MOTDNotificationMessageComposer
from communication.outgoing.handshake.session_params_message_composer import SessionParamsMessageComposer
from communication.outgoing.users.user_object_message_composer import UserObjectMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class InitCryptoMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(AuthenticationOKMessageComposer())
        user.send(SessionParamsMessageComposer())
        user.send(UserObjectMessageComposer())
        user.send(CreditBalanceMessageComposer())
        user.send(MOTDNotificationMessageComposer())
