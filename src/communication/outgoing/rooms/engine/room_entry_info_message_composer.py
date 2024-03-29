from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class RoomEntryInfoMessageComposer(MessageComposer):
    def __init__(self, is_private: bool, room_id: int, rights: bool):
        self.response = ServerMessage(src.communication.outgoing.header.RoomEntryInfoMessageComposer)
        self.is_private = is_private
        self.room_id = room_id
        self.rights = rights

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_boolean(self.is_private)  # is private room
        self.response.append_int32(self.room_id)  # room id
        self.response.append_boolean(self.rights)  # about rights
