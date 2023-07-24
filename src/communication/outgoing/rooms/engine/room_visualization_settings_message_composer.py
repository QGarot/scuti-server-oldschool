from src.communication.outgoing.message_composer import MessageComposer
from src.network.messages.server_message import ServerMessage
import src.communication.outgoing.header


class RoomVisualizationSettingsComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(src.communication.outgoing.header.RoomVisualizationSettingsComposer)

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_boolean(False)  # Hide wall
        self.response.append_int32(0)  # Wall thick
        self.response.append_int32(0)  # Floor thick
