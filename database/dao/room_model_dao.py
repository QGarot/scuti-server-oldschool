from database.database import Database
from game.rooms.models.room_model import RoomModel


class RoomModelDao:
    def __init__(self, db: Database):
        self.db = db

    def get_models(self) -> list[RoomModel]:
        """
        :return: Get room models from database
        """
        req = self.db.get("SELECT * FROM room_models")
        room_models = []
        for model in req:
            name = model[0]
            door_x = model[1]
            door_y = model[2]
            door_z = model[3]
            door_dir = model[4]
            height_map = model[5]
            room_model = RoomModel(name, door_x, door_y, int(door_z), door_dir, height_map)
            room_models.append(room_model)

        return room_models
