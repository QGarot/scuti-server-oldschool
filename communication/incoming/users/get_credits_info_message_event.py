from communication.incoming.message_event import MessageEvent
from communication.outgoing.users.credit_balance_message_composer import CreditBalanceMessageComposer
from communication.outgoing.users.habbo_activity_point_notification_message_composer import \
    HabboActivityPointNotificationMessageComposer
from game.users.user import User
from network.messages.client_message import ClientMessage


class GetCreditsInfoEvent(MessageEvent):
    @staticmethod
    def handle(user: User, request: ClientMessage) -> None:
        user.send(CreditBalanceMessageComposer(user.get_details().get_credits()))
        user.send(HabboActivityPointNotificationMessageComposer(0, user.get_details().get_pixels()))
        user.send(HabboActivityPointNotificationMessageComposer(4, user.get_details().get_shells()))

