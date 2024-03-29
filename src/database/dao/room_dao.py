from src.database.database import Database
from src.game.rooms.room import Room
from src.game.rooms.room_data import RoomData


class RoomDao:
    def __init__(self, db: Database):
        self.db = db

    def get_rooms(self) -> list[Room]:
        """
        :return: list of rooms registered in database
        """
        req = self.db.get("SELECT id,"
                          "roomtype,"
                          "caption,"
                          "owner,"
                          "description,"
                          "category,"
                          "state,"
                          "users_now,"
                          "users_max,"
                          "model_name,"
                          "score,"
                          "tags,"
                          "icon_bg,"
                          "icon_fg,"
                          "icon_items,"
                          "password,"
                          "wallpaper,"
                          "floor,"
                          "landscape FROM rooms")
        rooms = []
        for k in req:
            room = Room()
            room.set_room_data(RoomData(k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8], k[9], k[10], k[11], k[12], k[13], k[14], k[15], k[16], k[17], k[18]))
            rooms.append(room)

        return rooms

    def update_visitor(self, room_id: int, current_visitor_number: int) -> None:
        """
        :return:
        """
        self.db.update("rooms", {"users_now": current_visitor_number}, "id = " + str(room_id) + "")

