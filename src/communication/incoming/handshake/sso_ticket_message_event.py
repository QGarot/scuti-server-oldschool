from src.communication.incoming.message_event import MessageEvent
from src.communication.outgoing.handshake.auth_ok_message_composer import AuthenticationOKMessageComposer
from src.game.users.user import User
from src.game.users.user_manager import UserManager
from src.network.messages.client_message import ClientMessage
from src.communication.outgoing.users.motd_notification_message_composer import MOTDNotificationMessageComposer


class SSOTicketMessageEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage):
        sso = request.pop_fixed_string()
        print("Trying to connect with SSO: " + sso)
        # user.send(IgnoredUsersMessageComposer())
        if UserManager.get_instance().get_dao().login_sso(user, sso):
            UserManager.get_instance().connect_user(user)
            user.send(AuthenticationOKMessageComposer())
            user.send(MOTDNotificationMessageComposer())
        else:
            UserManager.get_instance().disconnect(user)
