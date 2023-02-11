from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class RoomPropertyMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(46)

    def get_response(self) -> ServerMessage:
        return self.response

    def compose(self):
        self.response.append_string_with_break("wallpaper")
        self.response.append_string_with_break("0.0")

        self.response.append_string_with_break("floor")
        self.response.append_string_with_break("0.0")

        self.response.append_string_with_break("landscape")
        self.response.append_string_with_break("0.0")
