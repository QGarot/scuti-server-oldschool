from game.rooms.room_data import RoomData


class Room:
    def __init__(self):
        self.room_data = RoomData()

        self.entity = []
        self.item = []

    def get_room_data(self) -> RoomData:
        return self.room_data


