from database.database import Database
from game.navigator.public_room import PublicRoom


class NavigatorDao:
    def __init__(self, db: Database):
        self.db = db

    def get_public_rooms(self) -> list[PublicRoom]:
        req = self.db.get("SELECT * FROM navigator_publics ORDER BY ordernum")
        res = []

        for public_room in req:
            id = public_room[0]
            order_num = public_room[1]
            banner_type = public_room[2]
            caption = public_room[3]
            image = public_room[4]
            image_type = public_room[5]
            room_id = public_room[6]
            category = public_room[7]
            category_parent_id = public_room[8]

            res.append(PublicRoom(banner_type, banner_type, caption, image, image_type, room_id, 0, category, id))

        return res
