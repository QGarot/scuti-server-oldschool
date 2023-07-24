from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.handshake.session_params_message_composer import SessionParamsMessageComposer
from src.game.users.user import User
from src.network.messages.client_message import ClientMessage


class InitCryptoMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        #user.send(AuthenticationOKMessageComposer())
        #user.send(SessionParamsMessageComposer())
        #user.send(UserObjectMessageComposer())
        #user.send(CreditBalanceMessageComposer())
        #user.send(MOTDNotificationMessageComposer())
        user.send(SessionParamsMessageComposer())
