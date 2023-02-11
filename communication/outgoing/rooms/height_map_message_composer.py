from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
from game.rooms.room_model import model


# todo: refactor this
class FloorHeightMapMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(470)

    def compose(self):
        # just for some tests...
        model.floor_height_map(self.response)

    def get_response(self) -> ServerMessage:
        return self.response


class HeightMapMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(31)

    def compose(self):
        self.response.append_string(model.string_builder())

    def get_response(self) -> ServerMessage:
        return self.response
