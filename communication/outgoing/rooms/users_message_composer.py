import communication.outgoing.header
from communication.outgoing.message_composer import MessageComposer
from game.users.user import User
from game.users.user_details import UserDetails
from network.messages.server_message import ServerMessage


class UsersMessageComposer(MessageComposer):
    def __init__(self, user: User):
        self.response = ServerMessage(communication.outgoing.header.UsersMessageComposer)
        self.user_details = user.get_details()
        self.user_pos = {
            "pos_x": user.pos_x,
            "pos_y": user.pos_y,
            "pos_z": user.pos_z
        }

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_int32(1)

        self.response.append_int32(self.user_details.get_id())
        self.response.append_string_with_break(self.user_details.get_username())
        self.response.append_string_with_break(self.user_details.get_motto())
        self.response.append_string_with_break(self.user_details.get_figure())
        self.response.append_int32(1)
        self.response.append_int32(self.user_pos["pos_x"])
        self.response.append_int32(self.user_pos["pos_y"])
        self.response.append_string_with_break(str(self.user_pos["pos_z"]))
        self.response.append_int32(2)
        self.response.append_int32(1)
        self.response.append_string_with_break(self.user_details.get_sex())
        self.response.append_int32(-1)
        self.response.append_int32(1)
        self.response.append_int32(-1)
        self.response.append_string_with_break("")
        self.response.append_int32(0)
