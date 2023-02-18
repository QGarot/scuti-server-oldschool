from database.database import Database
from game.rooms.models.room_model_manager import RoomModelManager
from game.rooms.room_manager import RoomManager
from game.users.user_manager import UserManager
from network.server import Server

print("Scuti Server - Oldschool 1.0")
# ~~~~~~~ Database ~~~~~~~
db = Database("localhost", "root", "", "scuti")

# ~~~~~~~ Managers ~~~~~~~
# Users
UserManager.get_instance()
UserManager.get_instance().set_dao(db)
# Rooms
RoomModelManager.get_instance()
RoomModelManager.get_instance().set_dao(db)
RoomModelManager.get_instance().load_models()

RoomManager.get_instance()
RoomManager.get_instance().set_dao(db)
RoomManager.get_instance().load_rooms()

# ~~~~~~~ Server ~~~~~~~
server = Server("127.0.0.1", 35000)
print(">> Server on!")
