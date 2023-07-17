from communication.outgoing.message_composer import MessageComposer
from network.messages.server_message import ServerMessage
from game.rooms.models.room_model import RoomModel
import communication.outgoing.header


class FloorHeightMapMessageComposer(MessageComposer):
    def __init__(self, model: RoomModel):
        self.response = ServerMessage(communication.outgoing.header.FloorHeightMapMessageComposer)
        self.model = model

    def compose(self):
        lines = self.model.height_map.split("\r")
        for y in range(self.model.map_size_y):
            line = lines[y]
            for x in range(self.model.map_size_x):
                tile = line[x]
                if x == self.model.door_x and y == self.model.door_y:
                    self.response.append_string(str(int(self.model.door_z)))
                else:
                    self.response.append_string(tile)
            self.response.append_string("\r")

    def get_response(self):
        return self.response


class HeightMapMessageComposer(MessageComposer):
    def __init__(self, model: RoomModel):
        self.response = ServerMessage(communication.outgoing.header.HeightMapMessageComposer)
        self.model = model

    def compose(self):
        self.response.append_string(self.model.height_map)

    def get_response(self):
        return self.response
