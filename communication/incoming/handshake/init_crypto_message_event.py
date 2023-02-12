from communication.incoming.message_event import MessageEvent
from communication.outgoing.handshake.session_params_message_composer import SessionParamsMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class InitCryptoMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        #user.send(AuthenticationOKMessageComposer())
        #user.send(SessionParamsMessageComposer())
        #user.send(UserObjectMessageComposer())
        #user.send(CreditBalanceMessageComposer())
        #user.send(MOTDNotificationMessageComposer())
        user.send(SessionParamsMessageComposer())
