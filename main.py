from database.database import Database
from game.users.user_manager import UserManager
from network.server import Server

# Database
db = Database("localhost", "root", "", "scuti")

# Managers
UserManager.get_instance()
UserManager.get_instance().set_dao(db)


server = Server("127.0.0.1", 35000)
print(">> Server on!")
