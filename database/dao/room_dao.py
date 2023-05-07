from database.database import Database
from game.rooms.room import Room


class RoomDao:
    def __init__(self, db: Database):
        self.db = db

    def get_rooms(self) -> list[Room]:
        """
        :return: list of rooms registered in database
        """
        req = self.db.get("SELECT id, roomtype, caption, owner, description, category, state, users_now, users_max, model_name, score, tags, icon_bg, icon_fg, icon_items, password, wallpaper, floor, landscape FROM rooms")
        rooms = []
        for k in req:
            room = Room()
            room.get_room_data().fill(k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8], k[9], k[10], k[11], k[12], k[13], k[14], k[15], k[16], k[17], k[18])
            rooms.append(room)

        return rooms
