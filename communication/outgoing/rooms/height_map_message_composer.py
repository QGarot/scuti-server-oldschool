from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
from game.rooms.models.room_model import model_b as model
import communication.outgoing.header


class FloorHeightMapMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.FloorHeightMapMessageComposer)

    def compose(self):
        lines = model.height_map.split("\r")
        for y in range(model.map_size_y):
            line = lines[y]
            for x in range(model.map_size_x):
                tile = line[x]
                if x == model.door_x and y == model.door_y:
                    self.response.append_string(str(int(model.door_z)))
                else:
                    self.response.append_string(tile)
            self.response.append_string("\r")

    def get_response(self):
        return self.response


class HeightMapMessageComposer(MessageComposer):
    def __init__(self):
        self.response = ServerMessage(communication.outgoing.header.HeightMapMessageComposer)

    def compose(self):
        self.response.append_string(model.height_map)

    def get_response(self):
        return self.response
