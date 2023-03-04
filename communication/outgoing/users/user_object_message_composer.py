from communication.outgoing.message_composer import MessageComposer
from game.users.user import UserDetails
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class UserObjectMessageComposer(MessageComposer):

    def __init__(self, user_details: UserDetails):
        self.response = ServerMessage(communication.outgoing.header.UserObjectMessageComposer)
        self.user_details = user_details

    def compose(self):
        self.response.append_string_with_break(str(self.user_details.get_id()))  # id
        self.response.append_string_with_break(self.user_details.get_username())  # username
        self.response.append_string_with_break(self.user_details.get_figure())  # look
        self.response.append_string_with_break(self.user_details.get_sex())  # sex
        self.response.append_string_with_break(self.user_details.get_motto())  # custom data (description)
        self.response.append_string_with_break(self.user_details.get_username())  # real name
        self.response.append_boolean(False)

        # TODO: work on respects
        self.response.append_int32(10)  # respect total
        self.response.append_int32(10)  # respect left
        self.response.append_int32(10)  # pet respect left
        self.response.append_boolean(False)  # stream publishing allowed

    def get_response(self):
        return self.response
