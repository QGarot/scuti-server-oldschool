import communication.outgoing.header
from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage


class RoomVisualizationSettingsComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.RoomVisualizationSettingsComposer)

    def get_response(self):
        return self.response

    def compose(self):
        self.response.append_boolean(False)  # Hide wall
        self.response.append_int32(0)  # Wall thick
        self.response.append_int32(0)  # Floor thick
