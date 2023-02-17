import communication.outgoing.header
from communication.outgoing.message_composer import MessageComposer
from game.users.user_details import UserDetails
from network.messages.server_message import ServerMessage


class UsersMessageComposer(MessageComposer):
    def __init__(self, user_details: UserDetails):
        self.response = ServerMessage(communication.outgoing.header.UsersMessageComposer)
        self.user_details = user_details

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_int32(1)

        self.response.append_int32(self.user_details.get_id())
        self.response.append_string_with_break(self.user_details.get_username())
        self.response.append_string_with_break(self.user_details.get_motto())
        self.response.append_string_with_break(self.user_details.get_figure())
        self.response.append_int32(1)
        self.response.append_int32(0)
        self.response.append_int32(23)
        self.response.append_string_with_break("2.0")
        self.response.append_int32(2)
        self.response.append_int32(1)
        self.response.append_string_with_break(self.user_details.get_sex())
        self.response.append_int32(-1)
        self.response.append_int32(1)
        self.response.append_int32(-1)
        self.response.append_string_with_break("")
        self.response.append_int32(0)
