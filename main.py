from database.database import Database
from game.catalog.catalog_manager import CatalogManager
from game.furnitures.furniture_manager import FurnitureManager
from game.navigator.navigator_manager import NavigatorManager
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
# Navigator
NavigatorManager.get_instance()
NavigatorManager.get_instance().set_dao(db)
#NavigatorManager.get_instance().load_public_rooms()
# Catalog
CatalogManager.get_instance()
CatalogManager.get_instance().set_dao(db)
CatalogManager.get_instance().load_pages()
CatalogManager.get_instance().load_catalog_items()

# Items
FurnitureManager.get_instance()
FurnitureManager.get_instance().set_dao(db)
FurnitureManager.get_instance().load_furnitures()

# ~~~~~~~ Server ~~~~~~~
server = Server("127.0.0.1", 35000)
print(">> Server on!")
print("-----------------------------------")
