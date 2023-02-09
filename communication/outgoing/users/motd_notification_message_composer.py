from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
import communication.outgoing.header


class MOTDNotificationMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.MOTDNotifMessageComposer)

    def compose(self):
        self.response.append_int32(5)
        self.response.append_string_with_break("Welcome to Scuti Oldschool!")
        self.response.append_string_with_break("")
        self.response.append_string_with_break("")
        self.response.append_string_with_break("")
        self.response.append_string_with_break("")

    def get_response(self):
        return self.response
