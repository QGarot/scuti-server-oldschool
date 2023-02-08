from communication.incoming.message_event import MessageEvent
from communication.outgoing.handshake.AuthenticationOKMessageComposer import AuthenticationOKMessageComposer
from communication.outgoing.users.CreditBalanceMessageComposer import CreditBalanceMessageComposer
from communication.outgoing.users.MOTDNotificationMessageComposer import MOTDNotificationMessageComposer
from communication.outgoing.handshake.SessionParamsMessageComposer import SessionParamsMessageComposer
from communication.outgoing.users.UserObjectComposer import UserObjectMessageComposer
from game.user.user import User
from network.messages.client_message import ClientMessage


class InitCryptoMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        user.send(AuthenticationOKMessageComposer())
        user.send(SessionParamsMessageComposer())
        user.send(UserObjectMessageComposer())
        user.send(CreditBalanceMessageComposer())
        user.send(MOTDNotificationMessageComposer())
