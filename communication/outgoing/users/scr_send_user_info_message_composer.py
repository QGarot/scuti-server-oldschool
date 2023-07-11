from communication.outgoing.message_composer import MessageComposer
from game.users.components.club_subscription import ClubSubscription
from network.messages.server_message import ServerMessage


class ScrSendUserInfoMessageComposer(MessageComposer):
    def __init__(self, club_subscription: ClubSubscription):
        self.response = ServerMessage(7)
        self.club_subscription = club_subscription

    def get_response(self) -> ServerMessage:
        return self.response

    def compose(self) -> None:
        self.response.append_string_with_break("habbo_club")
        self.response.append_int32(self.club_subscription.get_days_left())
        self.response.append_boolean(True)
        self.response.append_int32(-1)  # idk
        self.response.append_boolean(True)
        self.response.append_boolean(True)
        self.response.append_boolean(self.club_subscription.get_subscription_type() == "vip")
        self.response.append_int32(0)
        self.response.append_int32(0)
