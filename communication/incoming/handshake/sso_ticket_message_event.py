from communication.incoming.message_event import MessageEvent
from communication.outgoing.handshake.auth_ok_message_composer import AuthenticationOKMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class SSOTicketMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        print("Trying to connect with SSO: " + request.pop_fixed_string())
        # user.send(IgnoredUsersMessageComposer())
        user.send(AuthenticationOKMessageComposer())
