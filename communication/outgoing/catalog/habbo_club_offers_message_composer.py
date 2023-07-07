from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class HabboClubOffersMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(625)

    def get_response(self) -> ServerMessage:
        return self.response

    def compose(self) -> None:
        self.response.append_int32(4)  # Number of offers

        self.response.append_int32(4533)  # offer id (catalog_item id)
        self.response.append_string_with_break("HABBO_CLUB_BASIC_1_MONTH")  # Product code
        self.response.append_int32(15)  # Cost
        self.response.append_int32(0)  # Upgraded?
        self.response.append_int32(0)  # Is vip?
        self.response.append_int32(1)  # Periods
        self.response.append_int32(31)  # Days left after purchase
        self.response.append_int32(2023)  # YEAR
        self.response.append_int32(8)  # MONTH
        self.response.append_int32(5)  # DAY

        self.response.append_int32(4534)  # offer id
        self.response.append_string_with_break("HABBO_CLUB_BASIC_3_MONTHS")  # Product code
        self.response.append_int32(45)  # Cost
        self.response.append_int32(0)  # Upgraded?
        self.response.append_int32(0)  # Is vip?
        self.response.append_int32(3)  # Periods
        self.response.append_int32(93)  # Days of HabboClub
        self.response.append_int32(1)  # YEAR
        self.response.append_int32(1)  # MONTH
        self.response.append_int32(1)  # DAY

        self.response.append_int32(4535)  # offer id
        self.response.append_string_with_break("HABBO_CLUB_VIP_1_MONTH")  # Product code
        self.response.append_int32(25)  # Cost
        self.response.append_int32(0)  # Upgraded?
        self.response.append_int32(1)  # Is vip?
        self.response.append_int32(1)  # Periods
        self.response.append_int32(101)  # Days of HabboClub
        self.response.append_int32(1)  # YEAR
        self.response.append_int32(1)  # MONTH
        self.response.append_int32(1)  # DAY

        self.response.append_int32(4536)  # offer id
        self.response.append_string_with_break("HABBO_CLUB_VIP_3_MONTHS")  # Product code
        self.response.append_int32(60)  # Cost
        self.response.append_int32(0)  # Upgraded?
        self.response.append_int32(1)  # Is vip?
        self.response.append_int32(3)  # Periods
        self.response.append_int32(163)  # Days of HabboClub
        self.response.append_int32(1)  # YEAR
        self.response.append_int32(1)  # MONTH
        self.response.append_int32(1)  # DAY
