from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class ChatMessageComposer(MessageComposer):
    def __init__(self, user_id: int, message: str):
        self.response = ServerMessage(src.communication.outgoing.header.ChatMessageComposer)
        # self.room_id = room_id
        self.user_id = user_id
        self.message = message

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_int32(self.user_id)  # user id
        self.response.append_string_with_break(self.message)
